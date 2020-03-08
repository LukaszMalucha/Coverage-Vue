<template>
<div id="page-index">
    <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-cards">
            <div class="card document-description">

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
            document.title = this.document.document_name;

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