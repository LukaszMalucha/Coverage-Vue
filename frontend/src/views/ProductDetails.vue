<template>
<div id="page-index">
    <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-cards">
            <div class="card card-description">
                <div class="row plain-element text-left row-back">
                    <router-link :to="{ name: 'brand-details', params: {brand: product.product_brand}}">
                    <i class="fas fa-chevron-left"></i> Back To Search
                    </router-link>
                </div>
                <div class="row plain-element">
                    <div class="col s5 m5 l5 plain-element text-left">
                        <div class="row plain-element text-left" style="display:block">
                            <img :src="'/static/img/products/sample' + product.image + '.jpg'" class="img responsive img-description">
                        </div>
                        <br>
                        <div class="row plain-element text-left" style="display:block">
                            <img src="/static/img/products/sample2.jpg" class="img responsive">
                            <img src="/static/img/products/sample3.jpg" class="img responsive">
                            <img src="/static/img/products/sample4.jpg" class="img responsive">
                        </div>

                    </div>
                    <div class="col s6 m7 l7 plain-element">
                        <div class="row plain-element text-left">
                            <h4>{{ product.product_name}}</h4>
                            <h5>by <router-link :to="{ name: 'brand-details', params: {brand: product.product_brand}}">
                                    {{ product.product_brand}}
                                   </router-link> </h5>
                        </div>
                        <div class="row row-functions text-left">
                            <a class="btn btn-document" href="">
                                <i class="fas fa-file-pdf"></i> &nbsp; Document in PDF
                            </a>
                            <a class="btn btn-document" href="">
                                <i class="fas fa-file-code"></i> &nbsp; Document in HTML
                            </a>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Category: </h6>
                            <p>{{ product.product_category}}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Product Codes: </h6>
                            <p>{{ product.product_code}}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Product Series: </h6>
                            <p>{{ product.product_series}}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Part Number: </h6>
                            <p>{{ product.product_part_number}}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Business:  </h6>
                            <p>{{ product.business}}</p>
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
  components: {
  },
  props: {
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
    getProductData() {
    let endpoint = `/api/products/product/${this.id}/`;
    apiService(endpoint)
        .then(data => {
          window.console.log(endpoint);
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
  created() {
    this.getProductData();
  }
}
</script>