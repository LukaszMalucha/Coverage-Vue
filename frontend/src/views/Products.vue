<template>
<div id="page-index">
  <div class="row plain-element">
    <SidebarComponent
      :active = active
    />
    <div class="col s12 m5 col-content plain-element">
      <div class="row header">
        <div class="row searchbox-wrapper searchbox-long">
          <form @submit.prevent="submitQuery">
            <input class="form-control" id="searchbox" type="text" placeholder="Search for Product"
                   aria-label="Search for product" v-model="searchQuery">
            <button class="btn-transparent" type="submit"><i class="fas fa-search search-icon"></i></button>
          </form>
        </div>
      </div>
      <div class="dashboard-cards">

        <div id="formError" class="row row-error text-center">
          <p class="error" v-if="error">{{ error }}</p>
          <p v-show="loadingProducts">...loading...</p>
        </div>
        <div class="row row-documents" >
          <div class="row row-table-functions" >
            <div class="col s1 m3 l4 col-results plain-element left-align">
              <p class="resultCount" v-if="resultCount && filteredProductList.length > 0">{{ resultCount }}</p>
              <button v-if="resultCount && filteredProductList.length > 0" @click="csvExport()" class="btn btn-export">
                <i class="fas fa-file-download"></i>
              </button>
            </div>
            <div class="col s9 m6 l4 plain-element">
              <div v-if="productList.length > 0" id="tableSearch" class="filter-wrapper">
                <input id="keywordFilter" type="text" placeholder="Keyword Filter" class="place-holder-center"
                       v-model="search"/>
              </div>
            </div>
            <div class="col s3 m3 l4 plain-element right-align">
              <button v-if="resultCount && filteredProductList.length > 0" v-show="next" @click="submitQuery"
                      class="btn btn-loading">
                Load More
              </button>
            </div>
          </div>
          <div id="parent">
            <div id="child">
              <div v-for="(prod, index) in filteredProductList" :key="index" class="row plain-element">
                <a @click="getProductData(prod.id)">
                    <ProductCardComponent
                      :prod = prod
                      :index = index
                    />
                </a>
              </div>
             <div v-if="productList.length > 0" class="border-line"></div>
            </div>
          </div>
          <br>
          <div v-if="resultCount && filteredProductList.length > 0" class="row plain-element">
            <button v-show="next" @click="submitQuery" class="btn btn-loading">
              Load More
            </button>
          </div>
          <div v-if="resultCount && filteredProductList.length == 0" class="row plain-element">
            <h6>No results match search criteria</h6>
          </div>
        </div>
      </div>
    </div>
    <div class="col s12 m5 col-content-right plain-element" style="border-right: none;">
    <div v-if="documentList" class="plain-element">
        <ProductComponent
          :product = product
          :documentList = documentList
        />
      </div>

    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import SidebarComponent from "@/components/SidebarComponent.vue";
import ProductCardComponent from "@/components/ProductCardComponent.vue"
import ProductComponent from "@/components/ProductComponent.vue";

export default {
  name: "Products",
  components: {
    SidebarComponent,
    ProductCardComponent,
    ProductComponent
  },
  data() {
    return {
       error: null,
        resultCount: null,
        search: "",
        searchQuery: null,
        next: null,
        productList: [],
        documentList : null,
        loadingProducts: false,
        currentSearch: "",
        product: null,
        product_link: "",
        product_name: "",
        product_id: "",
        active: "products",
    }
  },
  methods: {
    submitQuery() {
        this.resultCount = null;
        this.search = "";
        if (!this.searchQuery) {
            this.error = "Search Field can't be empty";
            setTimeout(() => this.error = null, 3000);
        } else {
           if (this.searchQuery != this.currentSearch) {
              this.productList = [];
              this.next = null;
           }
           if (this.next) {
              endpoint = this.next;
           }

           let endpoint = `/api/products/products/?search=${this.searchQuery}`;
           if (this.next) {
              endpoint = this.next;
           }
           this.loadingproducts = true;
           apiService(endpoint)
            .then(data =>{
                if (data) {
                     this.resultCount = null;
                     this.loadingProducts = false;
                     this.error = null;
                     window.console.log(data);
                     this.productList.push(...data.results);
                     this.resultCount = data.count + " Results";
                     if(data.next) {
                        this.next = data.next;
                        } else {
                          this.next = null;
                        }
                     this.currentSearch = this.searchQuery;
                } else {
                    this.error = "No product has been found"
                }
            })
        }
    },
    getProductData(productId) {
      let endpoint = `/api/products/products/${productId}/`;
      apiService(endpoint)
          .then(data => {
            if (data) {
              this.product = data;
              this.getProductDocumentation(data.product_identifier)
              document.title = this.product.product_name;
            } else {
              this.product = null;
              document.title = "404 - Page Not Found"
            }
          })
      },
    getProductDocumentation(productIdentifier) {
      let endpoint = `/api/documents/?search=${productIdentifier}`;
      apiService(endpoint)
          .then(data => {
            window.console.log(endpoint);
            window.console.log(data);
            if (data) {
              this.documentList = data.results;

            } else {
              this.documentList = null;

            }
          })
    },

  },
  filters: {
//  Just in case if some strings would be too long and would destroy a layout
      truncatechars (value, limit) {
        if (value) {
            if (value.length > limit) {
              value = value.substring(0, limit) + "...";
              }
              return value
          }
        }
  },
  computed: {

    filteredProductList() {
      return this.productList.filter(product => {
        return product.product_name.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_brand.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_category.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_code.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_series.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_part_number.toLowerCase().includes(this.search.toLowerCase()) ||
               product.business.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    document.title = "Product Search";
  }
}

</script>