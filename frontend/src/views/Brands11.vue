<template>
  <div id="page-index">
    <div class="row header">
      <input class="form-control" id="searchbox" type="text" placeholder="Search for Brand"
             aria-label="Search for Brand" v-model="search">
    </div>
    <div class="dashboard-cards">
      <div v-if="filteredBrandList.length > 0" class="row row-cards">
        <div v-for="(brand, i) in filteredBrandList" :key="i" class="col s6 m3 l2 plain-element">
          <router-link :to="{ name: 'brand-details', params: {brand: brand}}">
            <div class="card company-card">
              <div class="card-image"><img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + brand + '.png'" class="img responsive">
              </div>
            </div>
          </router-link>
        </div>
      </div>
      <div v-else class="row row-cards">
        <h6>No results match search criteria</h6>
      </div>
    </div>
  </div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Brands",
  data() {
    return {
        search: '',
        brandsList: [],
    }
  },
  methods: {
//  Method that makes API call and retrieve a list of brands currently available in database
    getBrandList() {
    let endpoint = "/api/products/brand-list/";
    apiService(endpoint)
        .then(data => {
            if (data) {
            this.brandsList = data.brand_list
            } else {
                this.brandsList = [];
                document.title = "404 - Not Found"
            }
        })
    },
  },
  computed: {
    //  Filter brand list function
    filteredBrandList() {
      return this.brandsList.filter(brand => {
        return brand.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    document.title = "Johnson Controls Brands";
    this.getBrandList();
  }
}

</script>