<template>
  <div id="page-index">
    <div v-if="brandListContains(brand)" class="dashboard-cards">
      <div class="row row-break">

      </div>
      <div class="row row-cards">
        <div class="row">
          <div class="col s2 m2 l2 left-align col-brand">
            <a @click="reloadQuery">
              <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + brand + '.png'" class="img responsive img-banner">
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

        <div v-if="productList.length > 0" class="row plain-element">
          <div class="row plain-element row-table-functions">
            <div class="col s3 m4 l4 col-results plain-element left-align">
              <p class="productCount" v-if="resultCount && filteredProductList.length > 0">{{ resultCount }}</p>
            </div>
            <div class="col s8 m4 l4 plain-element">
              <div id="productSearch" class="filter-wrapper">
                <input type="text" placeholder="Keyword Filter" class="place-holder-center center-align"
                       v-model="productSearch"/>
              </div>
            </div>
            <div v-if="filteredProductList.length > 0" class="col s4 m4 l4 plain-element right-align">
              <button v-show="next" @click="getBrandData" class="btn btn-loading">
                Load More
              </button>
            </div>
          </div>
          <div class="row plain-element">
            <div class="col s6 m3 l2 plain-element col-product" v-for="product in filteredProductList"
                 :key="product.pk">
              <router-link :to="{ name: 'product-details', params: {id: product.id}}">
                <div class="card card-product" :name="product.product_name"
                     :code="product.product_code" :category="product.product_category"
                     :series="product.product_series" :part_number="product.product_part_number"
                     :business="product.business">
                  <div class="card-image">
                    <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + product.image + '.jpg'">
                  </div>
                  <div class="card-content">
                    <span class="card-title">{{ product.product_name|truncatechars(88) }}</span>
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
          <div v-if="filteredProductList.length == 0" class="row plain-element">
            <h6>No results match search criteria</h6>
          </div>
        </div>
        <div v-if="queryList.length > 0" class="row plain-element">
            <div class="row plain-element row-table-functions">
              <div class="col s3 m4 l4 col-results plain-element left-align">
                <p class="productCount" v-if="resultCount && filteredQueryList.length > 0">{{ resultCount }}</p>
              </div>
              <div class="col s8 m4 l4 plain-element">
                <div id="productSearch" class="filter-wrapper">
                  <input type="text" placeholder="Keyword Filter" class="place-holder-center center-align"
                         v-model="querySearch"/>
                </div>
              </div>
              <div v-if="filteredQueryList.length > 0" class="col s4 m4 l4 plain-element right-align">
                <button v-show="nextQuery" @click="submitQuery" class="btn btn-loading">
                  Load More
                </button>
              </div>
            </div>
            <div class="row plain-element">
              <div class="col s6 m3 l2 plain-element col-product" v-for="product in filteredQueryList" :key="product.pk">
                <router-link :to="{ name: 'product-details', params: {id: product.id}}">
                  <div class="card card-product" :name="product.product_name"
                       :code="product.product_code" :category="product.product_category"
                       :series="product.product_series" :part_number="product.product_part_number"
                       :business="product.business">
                    <div class="card-image">
                      <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + product.image + '.jpg'">
                    </div>
                    <div class="card-content">
                      <span class="card-title">{{ product.product_name|truncatechars(88) }}</span>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>
            <div v-if="filteredQueryList.length > 0" class="row plain-element">
              <p v-show="loadingProducts">...loading...</p>
              <button v-show="nextQuery" @click="submitQuery" class="btn btn-loading">
                Load More
              </button>
            </div>
            <div v-if="filteredQueryList.length == 0" class="row plain-element">
              <h6>No results match search criteria</h6>
            </div>
        </div>
      </div>
    </div>
    <div v-else>
        <NotFoundComponent/>
    </div>

  </div>
</template>

<script>
import { cleanBrandList } from "@/common/brands.js"
import { brandMapperDict } from "@/common/brandmapper.js"
import { apiService } from "@/common/api.service.js";
import NotFoundComponent from "@/components/NotFoundComponent.vue"

export default {
  name: "Products",
  components: {
    NotFoundComponent
  },
  props: {
//  Get brand string passed from previous view
     brand: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      productSearch: "",
      querySearch: "",
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
      brandList : cleanBrandList,
      brandMapperDict : brandMapperDict,
    }
  },
  methods: {

//  Method that initially fill the view with all products belonging to the brand
    async getBrandData() {

//      this.brand =  this.getOriginalBrand(this.brand)
      let endpoint = `/api/products/products/?product_brand=${this.getOriginalBrand}`;
      if (this.next) {
        //  Check if API returns multiple pages
        endpoint = this.next;
      }
      this.loadingProducts = true;
      await apiService(endpoint)
       .then(data => {
          if (data) {
              this.queryList = [];
              this.productList.push(...data.results);
              this.resultCount = data.count + " Products";
              this.loadingProducts = false;
              // Stop loading more if user already on the last page
              if(data.next) {
                this.next = data.next;
              } else {
                this.next = null;
              }
          }else {
            this.productList = [];
            document.title = "404 - Not Found"
          }
        }).then (
          window.console.log(this.productList)
        )
      },
//  Function that searches for data within given brand
    async submitQuery() {
       if (!this.searchQuery) {
            this.error = "Search Field can't be empty";
            setTimeout(() => this.error = null, 3000);
       } else {
           if (this.searchQuery != this.currentSearch ) {
              this.queryList = [];
              this.nextQuery = null;
           }
           this.next = false;
           let endpoint = `/api/products/products/?product_brand=${this.getOriginalBrand}&search=${this.searchQuery}`;
           if (this.nextQuery) {
              endpoint = this.nextQuery;
           }
           if (!this.nextQuery) {
              this.queryList = [];
           }
           this.loadingProducts = true;
           await apiService(endpoint)
           .then(data => {
              if (data) {
                  this.productList = [];
                  this.queryList.push(...data.results);
                  this.resultCount = data.count + " Products";
                  this.loadingProducts = false;
                  // Stop loading more if user already on the last page
                  if(data.next) {
                    this.nextQuery = data.next;
                  } else {
                    this.nextQuery = null;
                  }
                  this.currentSearch = this.searchQuery;
              } else {
                this.product = null;
                document.title = "404 - Page Not Found"
              }
            }).then (
              window.console.log(this.queryList)
            )
        }
    },
//  Function that handles clicking company banner in the top-left corner
    reloadQuery(){
      this.productList = [];
      this.queryList = [];
      this.next = false;
      this.getBrandData();
    },
     brandListContains(n) {
       return this.brandList.indexOf(n) > -1
     },
  },
  computed: {
//  Dynamic filter for the listed products (all fields included)
    filteredProductList() {
      return this.productList.filter(product => {
        return product.product_name.toLowerCase().includes(this.productSearch.toLowerCase()) ||
               product.product_category.toLowerCase().includes(this.productSearch.toLowerCase()) ||
               product.product_code.toLowerCase().includes(this.productSearch.toLowerCase()) ||
               product.product_series.toLowerCase().includes(this.productSearch.toLowerCase()) ||
               product.product_part_number.toLowerCase().includes(this.productSearch.toLowerCase()) ||
               product.business.toLowerCase().includes(this.productSearch.toLowerCase())
      })
    },
    filteredQueryList() {
      return this.queryList.filter(product => {
        return product.product_name.toLowerCase().includes(this.querySearch.toLowerCase()) ||
               product.product_category.toLowerCase().includes(this.querySearch.toLowerCase()) ||
               product.product_code.toLowerCase().includes(this.querySearch.toLowerCase()) ||
               product.product_series.toLowerCase().includes(this.querySearch.toLowerCase()) ||
               product.product_part_number.toLowerCase().includes(this.querySearch.toLowerCase()) ||
               product.business.toLowerCase().includes(this.querySearch.toLowerCase())
      })
    },
//    Function that retrieve a brand 
    getOriginalBrand() {
        let cleanBrand = this.brandMapperDict[this.brand];
        return cleanBrand
    },
  },
 filters: {
//  Just in case if some strings would be too long and would destroy a layout
      truncatechars (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
  created() {
    this.getBrandData();
    document.title = this.getOriginalBrand + " Products";
  }
}

</script>