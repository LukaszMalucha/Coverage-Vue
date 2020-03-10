<template>
<div id="page-index">
    <div class="row header">
            <input class="form-control" id="searchbox" type="text" placeholder="Search for Brand"
                   aria-label="Search for Brand" v-model="search">
    </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
        <div v-for="(brand, i) in filteredList" :key="i" class="col s6 m3 l2 plain-element">
            <router-link :to="{ name: 'brand-details', params: {brand: brand}}">
                <div class="card company-card">
                    <div class="card-image"><img  :src="'/static/img/brands/' + brand + '.png'" class="img responsive">
                    </div>
                </div>
            </router-link>
        </div>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Brands",
  components: {

  },
  data() {
    return {
        search: '',
        brandsList: [],

    }
  },
  methods: {
    getBrandList() {
    let endpoint = "/api/products/brand-list/";
    apiService(endpoint)
        .then(data => {
            this.brandsList = data.brand_list

        })
    },
  },
  computed: {
    //  Search brand function
    filteredList() {
      return this.brandsList.filter(brand => {
        return brand.toLowerCase().includes(this.search.toLowerCase())
      })
    }

  },
  created() {
    document.title = "Brand Search";
    this.getBrandList();

  }


}
</script>