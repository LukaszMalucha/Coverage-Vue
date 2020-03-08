<template>
<div id="page-index">
    <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-cards">
            <div class="card card-description">
                <div class="row plain-element text-left row-back">
                    <router-link :to="{ name: 'brand-details', params: {brand: document.document_brand}}">
                    <i class="fas fa-chevron-left"></i> Back To Search
                    </router-link>
                </div>
                <br>
                <div class="row plain-element">
                    <div class="col s6 m6 l6 plain-element">
                        <div class="row plain-element text-left">
                            <h4>{{ document.document_title}}</h4>
                            <h5> {{ product_name }} </h5>
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
                            <h6>Document Number: </h6>
                            <p>{{ document.document_number }}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Document Version: </h6>
                            <p>{{ document.document_version }}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Document Type: </h6>
                            <p>{{ document.document_version }}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Date Created: </h6>
                            <p>{{ document.document_created_at}}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Last Edition:  </h6>
                            <p>{{ document.document_last_edition }}</p>
                        </div>
                        <div class="row plain-element text-left">
                            <h6>Last Publication: </h6>
                            <p>{{ document.document_last_publication }}</p>
                        </div>
                        {{document.topics}}
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
  name: "DocumentDetails",
  components: {
  },
  props: {
    id: {
      required: true
    }
  },
  data() {
    return {
      document: [],
      product_name: "",
    }
  },
  methods: {
    getDocumentData() {
    let endpoint = `/api/documents/${this.id}/`;
    apiService(endpoint)
        .then(data => {
          window.console.log(endpoint);
          window.console.log(data);
          if (data) {
            this.document = data;
            this.product_name = this.document.product['product_name']
            document.title = this.document.document_title;


          } else {
            this.document = null;
            document.title = "404 - Page Not Found"
          }
        })
    },
  },
  created() {
    this.getDocumentData();
  }
}
</script>