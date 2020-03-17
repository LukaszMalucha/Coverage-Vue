<template>
<div id="page-index">
<div class="dashboard-cards">
  <div class="row row-break">

  </div>

    <div class="row row-cards">
        <div class="row">
            <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 plain-element text-left">
                <a @click="getBrandData">
                    <img :src="'/static/img/brands/' + brand + '.png'" class="img responsive">
                </a>
            </div>
            <div class="col-xs-10 col-sm-10 col-md-10 col-lg-10 col-searchbox">
             <div class="row searchbox-wrapper-long">
                <form @submit.prevent="onSubmit">
                  <input class="form-control" id="searchbox" type="text" placeholder="Search for Product"
                         aria-label="Search for Product" v-model="searchQuery">
                    <button class="btn-transparent" type="submit"><i class="fas fa-search search-icon"></i></button>
                </form>
              </div>
            </div>
        </div>
        <div id="formError" class="row row-error text-center">
              <p class="error">{{ error }}</p>
        </div>
        <div class="row plain-element row-table-functions">
            <div class="col s1 m4 l4 col-results plain-element text-left">
                <p class="resultCount" v-if="resultCount">{{ resultCount }}</p>
            </div>
            <div class="col s10 m4 l4 plain-element">
              <div id="tableSearch" class="filter-wrapper">
                <input type="text" placeholder="Keyword Search" class="place-holder-center" v-model="search"/>
              </div>
            </div>
            <div class="col s1 m4 l4 plain-element">
            </div>
          </div>
        <div class="row plain-element">
            <table id="dataTable">
                <thead>
                    <tr v-if="filteredProductList.length > 0" class="table-header">
                      <th onclick="sortTable(0)" class="text-left field-long">Product Name</th>
                      <th onclick="sortTable(1)" class="text-center field-long">Product Codes</th>
                      <th onclick="sortTable(1)" class="text-center field-long">Product Category</th>
                      <th onclick="sortTable(3)" class="text-center field-long">Product Series</th>
                      <th onclick="sortTable(4)" class="text-center field-medium">Product Part Number</th>
                      <th onclick="sortTable(5)" class="text-center field-long">Business</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in filteredProductList" :key="product.pk">
                      <td class="text-left field-long">{{ product.product_name }}</td>
                      <td class="text-center field-long">{{ product.product_code }}</td>
                      <td class="text-center field-long">{{ product.product_category }}</td>
                      <td class="text-center field-long">{{ product.product_series }}</td>
                      <td class="text-center field-medium">{{ product.product_part_number }}</td>
                      <td class="text-center field-long">{{ product.business }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="col s6 m2 plain-element"  v-for="product in filteredProductList" :key="product.pk">
                <div class="card card-product" :code="product.product_code" :category="product.product_category"
                :series="product.product_series" :part_number="product.product_part_number" :business="product.business">
                    <div class="card-image">
                        <img src="/static/img/products/sample11.jpg">
                    </div>
                    <div class="card-content">
                        <span class="card-title">{{ product.product_name }}</span>
                    </div>
                </div>
            </div>

        </div>
        <div class="row plain-element ">
          <p v-show="loadingProducts">...loading...</p>
          <button v-show="next" @click="getBrandData" class="btn btn-loading">
          Load More
          </button>
        </div>
        <div class="row plain-element">
          <p v-show="loadingQuery">...loading...</p>
          <button v-show="nextQuery" @click="onSubmit" class="btn btn-loading">
          Load More
          </button>
        </div>
    </div>
</div>


</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Products",
  components: {

  },
  props: {
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
    }
  },
  methods: {
   async getBrandData() {
    if (this.searchQuery != null) {
        this.productList = [];
        this.searchQuery = null;
        this.loadingQuery = false;
    }
    let endpoint = `/api/products/${this.brand}/`;
    if (this.next) {
      endpoint = this.next;
    }
    this.loadingProducts = true;
    await apiService(endpoint)
     .then(data => {
        window.console.log(data);
        document.getElementById("tableSearch").style.display = "inline-table";
        document.getElementById("dataTable").style.display = "inline-table";
        this.productList.push(...data.results);
        this.resultCount = data.count + " Products";
        this.loadingProducts = false;
        if(data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      }).then (
        window.console.log(this.productList)
      )
    },
    onSubmit() {
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
           this.loadingQuery = true;
           let endpoint = `/api/products/${this.brand}/?search=${this.searchQuery}`;
           if (this.nextQuery) {
              endpoint = this.nextQuery;
            }
           let method = "GET"
           apiService(endpoint, method)
            .then(data =>{
                if (data) {
                     this.resultCount = null;
                     this.error = null;
                     window.console.log(data);
                     this.productList.push(...data.results);
                     this.loadingProducts = false;
                     this.loadingQuery = false;
                     this.resultCount = data.count + " Products";
                     document.getElementById("tableSearch").style.display = "inline-table"
                     document.getElementById("dataTable").style.display = "inline-table"
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
  },

  computed: {

    filteredProductList() {
      return this.productList.filter(product => {
        return product.product_name.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_category.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_code.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_series.toLowerCase().includes(this.search.toLowerCase()) ||
               product.product_part_number.toLowerCase().includes(this.search.toLowerCase()) ||
               product.business.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.getBrandData();
    document.title = "Brand Products";
  }
}
</script>