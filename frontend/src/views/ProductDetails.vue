<template>
<div id="page-index">
    <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-cards">
            <div class="card card-description">
                <div class="row left-align row-back">
                    <router-link :to="{ name: 'brand-details', params: {brand: product.clean_brand}}">
                    <i class="fas fa-chevron-left"></i> Back To Search
                    </router-link>
                </div>
                <div class="row plain-element">
                    <div class="col s2 m3 l5 plain-element left-align col-product-images">
                        <div class="row plain-element left-align">
                            <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + product.image + '.jpg'" class="img responsive img-description">
                        </div>
                        <br>
                        <div class="row plain-element left-align" style="display:block">
                          <div class="col s12 m12 l4 plain-element left-align">
                              <img src="https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample2.jpg" class="img img-small">
                          </div>
                          <div class="col s12 m12 l4 plain-element left-align">
                              <img src="https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample3.jpg" class="img img-small">
                          </div>
                          <div class="col s12 m12 l4 plain-element left-align">
                              <img src="https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample4.jpg" class="img img-small">
                          </div>
                        </div>

                    </div>
                    <div class="col s10 m9 l7 plain-element">
                        <div class="row plain-element left-align">
                            <h3>{{ product.product_name}}</h3>
                            <h5>by <router-link :to="{ name: 'brand-details', params: {brand: product.clean_brand}}">
                                    {{ product.product_brand}}
                                   </router-link> </h5>
                        </div>
                        <div class="row row-functions left-align">
                            <router-link class="btn btn-document" :to="{ name: 'documents', params: {productId: product.product_identifier}}">
                                <i class="fas fa-file-pdf"></i> &nbsp; Documentation
                            </router-link>
                        </div>
                        <div class="row plain-element left-align">
                            <h6>Category: </h6>
                            <p>{{ product.product_category| truncatechars(1000)}}</p>
                        </div>
                        <div class="row plain-element left-align">
                            <h6>Product Codes: </h6>
                            <p>{{ product.product_code| truncatechars(1000)}}</p>
                        </div>
                        <div class="row plain-element left-align">
                            <h6>Product Series: </h6>
                            <p>{{ product.product_series| truncatechars(1000)}}</p>
                        </div>
                        <div class="row plain-element left-align">
                            <h6>Part Number: </h6>
                            <p>{{ product.product_part_number| truncatechars(1000)}}</p>
                        </div>
                        <div class="row plain-element left-align">
                            <h6>Business:  </h6>
                            <p>{{ product.business| truncatechars(1000)}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "ProductDetails",
  props: {
//  Product Id that is being passed as a search query
    id: {
      required: true
    }
  },
  data() {
    return {
      product: [],
    }
  },
  methods: {
//  Method that retrieve product data
    getProductData() {
    let endpoint = `/api/products/product/${this.id}/`;
    apiService(endpoint)
        .then(data => {
          window.console.log(data);
          if (data) {
            this.product = data;
            document.title = this.product.product_name;
          } else {
            this.product = null;
            document.title = "404 - Page Not Found"
          }
        })
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
    this.getProductData();
  }
}
</script>