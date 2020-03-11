<template>
  <div id="page-index">
    <div class="dashboard-cards">
      <div class="row row-break">
      </div>
      <div class="row row-cards">
        <div class="row">
          <div class="col s2 m2 l2 left-align col-brand">
            <a @click="reloadQuery">
              <img :src="'/static/img/brands/' + brand + '.png'" class="img responsive img-banner">
            </a>
          </div>
          <div class="col s12 m12 l10 col-searchbox">
            <div class="row searchbox-wrapper-long">
              <form @submit.prevent="submitQuery">
                <input class="form-control" id="searchbox" type="text" placeholder="Search for Product"
                       aria-label="Search for Product" v-model="searchQuery">
                <button class="btn-transparent" type="submit"><i class="fas fa-search search-icon"></i></button>
              </form>
            </div>
          </div>
        </div>
        <div id="formError" class="row row-error text-center">
          <p class="error">{{ error }}</p>
          <p v-show="loadingQuery">...loading...</p>
        </div>
        <div class="row plain-element row-table-functions">
          <div class="col s3 m4 l4 col-results plain-element left-align">
            <p class="productCount" v-if="resultCount && filteredProductList.length > 0">{{ resultCount }}</p>
          </div>
          <div class="col s8 m4 l4 plain-element">
            <div id="productSearch" class="filter-wrapper">
              <input type="text" placeholder="Keyword Filter" class="place-holder-center" v-model="search"/>
            </div>
          </div>
          <div v-if="filteredProductList.length > 0" class="col s4 m4 l4 plain-element right-align">
            <button v-show="next" @click="getBrandData" class="btn btn-loading">
              Load More
            </button>
            <button v-show="nextQuery" @click="submitQuery" class="btn btn-loading">
              Load More
            </button>
          </div>
        </div>
        <div class="row plain-element">

          <div class="col s6 m3 l2 plain-element col-product" v-for="product in filteredProductList" :key="product.pk">
            <router-link :to="{ name: 'product-details', params: {id: product.id}}">
              <div class="card card-product" :name="product.product_name"
                   :code="product.product_code" :category="product.product_category"
                   :series="product.product_series" :part_number="product.product_part_number"
                   :business="product.business">
                <div class="card-image">
                  <img :src="'/static/img/products/sample' + product.image + '.jpg'">
                </div>
                <div class="card-content">
                  <span class="card-title">{{ product.product_name }}</span>
                </div>
              </div>
            </router-link>
          </div>

        </div>
        <div v-if="filteredProductList.length > 0" class="row plain-element">
          <p v-show="loadingProducts">...loading...</p>
          <button v-show="next" @click="getBrandData" class="btn btn-loading">
            Load More
          </button>
        </div>
        <div v-if="filteredProductList.length > 0" class="row plain-element">
          <button v-show="nextQuery" @click="submitQuery" class="btn btn-loading">
            Load More
          </button>
        </div>
        <div v-if="filteredProductList.length == 0" class="row plain-element">
          <h6>No results match search criteria</h6>

        </div>
      </div>
    </div>


  </div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Products",
  props: {
//  Get brand string passed from previous view
     brand: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      search: "",
      error: null,
      resultCount: null,
      searchQuery: null,
      productList: [],
      queryList: [],
      next: null,
      nextQuery: null,
      loadingProducts: false,
      loadingQuery: false,
      currentSearch: "",
      randomNumber : null,
    }
  },
  methods: {
//  Method that initially fill the view with all products belonging to the brand
    async getBrandData() {
      if (this.searchQuery != null) {
          // Clear the after previous query, otherwise it will get appended to existing list
          this.productList = [];
          this.loadingQuery = false;
          this.searchQuery = null;
      }
      let endpoint = `/api/products/${this.brand}/`;
      if (this.next) {
        //  Check if API returns multiple pages
        endpoint = this.next;
      }
      this.loadingProducts = true;
      await apiService(endpoint)
       .then(data => {
          window.console.log(data);
          document.getElementById("productSearch").style.display = "inline-table";
          this.productList.push(...data.results);
          this.resultCount = data.count + " Products";
          this.loadingProducts = false;
          // Stop loading more if user already on the last page
          if(data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        }).then (
          window.console.log(this.productList)
        )
      },
//  Thsi function is a copy of the one above, except that it handles specific user query (search = "Foam")
    submitQuery() {
        this.next = false;
        this.search = "";
        this.resultCount = "";
        if (!this.searchQuery) {
            this.error = "Search Field can't be empty";
            setTimeout(() => this.error = null, 3000);
        } else {
            if (this.searchQuery != this.currentSearch) {
              this.productList = [];
              this.nextQuery = null;
            }
            if (this.searchQuery == this.currentSearch && this.next == false) {
              this.productList = [];
              this.nextQuery = null;
            }
           this.loadingQuery = true;
           let endpoint = `/api/products/${this.brand}/?search=${this.searchQuery}`;
           if (this.nextQuery) {
              endpoint = this.nextQuery;
            }
           apiService(endpoint)
            .then(data =>{
                if (data) {
                     this.resultCount = null;
                     this.error = null;
                     window.console.log(data);
                     this.productList.push(...data.results);
                     this.loadingProducts = false;
                     this.loadingQuery = false;
                     this.resultCount = data.count + " Products";
                     document.getElementById("productSearch").style.display = "inline-table"
                     if(data.next) {
                        this.nextQuery = data.next;
                        } else {
                          this.nextQuery = null;
                        }
                     this.currentSearch = this.searchQuery;
                } else {
                    this.error = "No product has been found"
                }
            })
        }
    },
//  Function that handles clicking company banner in the top-left corner
    reloadQuery(){
      this.productList = [];
      this.next = false;
      this.getBrandData();
    }
  },
  computed: {
//  Dynamic filter for the listed products (all fields included)
    filteredProductList() {
      return this.productList.filter(product => {
        return product.product_name.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_category.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_code.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_series.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_part_number.toLowerCase().includes(this.search.toLowerCase()) ||
               product.business.toLowerCase().includes(this.search.toLowerCase())
      })
    },
  },
  created() {
    this.getBrandData();
    document.title = "Brand Products";
  }
}

</script>