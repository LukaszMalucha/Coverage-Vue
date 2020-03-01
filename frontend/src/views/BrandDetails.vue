<template>
<div id="page-index">
<div class="dashboard-cards">
  <div class="row row-break">

  </div>

    <div class="row row-cards">
        <div class="row">
            <div class="col-xs-8 col-sm-8 col-md-10 col-lg-10 plain-element text-left">
                <img :src="'/static/img/brands/' + brand + '.png'" class="img responsive">
            </div>
            <div class="col-xs-4 col-sm-4 col-md-2 col-lg-2 plain-element">
                <div class="search-wrapper">
                    <label> Search Table:</label>
                    <input type="text" v-model="search"/>
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
                      <td class="text-left field-long">{{ product.product_code }}</td>
                      <td class="text-left field-long">{{ product.product_series }}</td>
                      <td class="text-center field-medium">{{ product.product_part_number }}</td>
                      <td class="text-center field-medium">{{ product.business }}</td>
                    </tr>
                </tbody>
            </table>
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
    }
  },
  methods: {
   async getBrandData() {
    let endpoint = `/api/products/${this.brand}/`;
    await apiService(endpoint)
     .then(data => {
        window.console.log(data);
        this.productList = data.results;
      }).then (
        window.console.log(this.productList)
      )
    },
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