<template>
<div id="page-index">
<div class="dashboard-cards">
  <div class="row row-break">

  </div>

    <div class="row row-cards">
        <div class="row">
            <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 plain-element text-left">
                      <label> TABLE ONLY</label>
                      <input type="text" v-model="search"/>
            </div>
            <div class="col-xs-4 col-sm-4 col-md-2 col-lg-9 plain-element">
                <div class="search-wrapper">
                  <form @submit.prevent="onSubmit">
                      <label> QUERY</label>
                      <input type="text" v-model="searchQuery"/>
                  </form>
                </div>
            </div>
        </div>
        <div class="row plain-element">
            <table id="dataTable">
                <thead>
                    <tr>
                      <th onclick="sortTable(0)" class="text-left">Product Name</th>
                      <th onclick="sortTable(1)" class="text-left">Product Category</th>
                      <th onclick="sortTable(2)">Product Code</th>
                      <th onclick="sortTable(3)">Product Series</th>
                      <th onclick="sortTable(4)" class="text-center">Product Part Number</th>
                      <th onclick="sortTable(5)">Business</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in filteredProductList" :key="product.pk">
                      <td class="text-left field-medium">{{ product.product_name }}</td>
                      <td class="text-left field-medium">{{ product.product_category }}</td>
                      <td class="text-left field-long">{{ product.product_series }}</td>
                      <td class="text-center field-medium">{{ product.product_part_number }}</td>
                      <td class="text-center field-medium">{{ product.business }}</td>
                    </tr>
                    <tr v-for="product in queryList" :key="product.pk">
                      <td class="text-left field-medium">{{ product.product_name }}</td>
                      <td class="text-left field-medium">{{ product.product_category }}</td>
                      <td class="text-left field-long">{{ product.product_series }}</td>
                      <td class="text-center field-medium">{{ product.product_part_number }}</td>
                      <td class="text-center field-medium">{{ product.business }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="my-4">
              <p v-show="loadingProducts">...loading...</p>
              <button v-show="next" @click="getBrandData" class="btn btn-sm btn-success">
              GET DATA
              </button>
            </div>
            <br><br><br><br>
            <div class="my-4">
              <p v-show="loadingQuery">...loading...</p>
              <button v-show="nextQuery" @click="onSubmit" class="btn btn-sm btn-success">
                Submit
              </button>
            </div>
        </div>
    </div>
</div>


</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "BrandDetails",
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
      productList: [],
      queryList: [],
      next: null,
      nextQuery: null,
      loadingProducts: false,
      loadingQuery: false,
      searchQuery: null,
      currentSearch: "",
    }
  },
  methods: {
   async getBrandData() {
    let endpoint = `/api/products/${this.brand}/`;
    if (this.next) {
      endpoint = this.next;
    }
    this.loadingProducts = true;
    await apiService(endpoint)
     .then(data => {
        window.console.log(data);
        this.productList.push(...data.results);
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
        this.productList = [];
        if (this.searchQuery != this.currentSearch) {
          this.queryList = [];
          this.nextQuery = null;
        }
        window.console.log(this.searchQuery, this.currentSearch)
        let endpoint = `/api/products/${this.brand}/?search=${this.searchQuery}`;
        window.console.log(endpoint);
        if (this.nextQuery) {
          endpoint = this.nextQuery;
        }
        this.loadingQuery = true;
        apiService(endpoint)
        .then(data => {
            this.queryList.push(...data.results);
            window.console.log(data);
            this.loadingQuery = false;
             if(data.next) {
               this.nextQuery = data.next;
             } else {
               this.nextQuery = null;
             }
             this.currentSearch = this.searchQuery;
        })
    },
    clearList() {
      this.productList = [];
    }
  },
  computed: {
//  Search company function
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
    document.title = "Brand Data";
  }
}
</script>