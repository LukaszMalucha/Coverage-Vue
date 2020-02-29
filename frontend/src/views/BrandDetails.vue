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
            <table id="documentTable">
                <thead>
                    <tr>
                      <th onclick="sortTable(0)" class="text-left">Product Name</th>
                      <th onclick="sortTable(1)" class="text-left">Product Category</th>
                      <th onclick="sortTable(2)">Document Title</th>
                      <th onclick="sortTable(3)">Topic Title</th>
                      <th onclick="sortTable(4)" class="text-center">Document No.</th>
                      <th onclick="sortTable(5)" class="text-center">Created At</th>
                      <th onclick="sortTable(6)" class="text-center">Last Edition</th>
                      <th onclick="sortTable(7)" class="text-center">Link</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="document in filteredDocumentList" :key="document.pk">
                      <td class="text-left field-medium">{{ document.product_name }}</td>
                      <td class="text-left field-medium">{{ document.product_category }}</td>
                      <td class="text-left field-long">{{ document.document_title }}</td>
                      <td class="text-left field-long">{{ document.topic_title }}</td>
                      <td class="text-center field-medium">{{ document.document_number }}</td>
                      <td class="text-center field-short">{{ document.document_created_at }}</td>
                      <td class="text-center field-short">{{ document.document_last_edition }}</td>
                      <td class="text-center field-short"><a target="_blank" :href="'https://johnsoncontrols-uat.fluidtopics.net' + document.document_link"><i class="far fa-file-pdf fa-2x"></i></a></td>
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
      documentList: [],
    }
  },
  methods: {
   async getBrandData() {
    let endpoint = `/api/brands/${this.brand}/`;
    await apiService(endpoint)
     .then(data => {
        window.console.log(data);
        this.documentList = data.results;
      }).then (
        window.console.log(this.documentList)
      )
    },
  },
  computed: {
//  Search company function
    filteredDocumentList() {
      return this.documentList.filter(document => {
        return document.document_title.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_number.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product_name.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product_category.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_created_at.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_last_edition.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.getBrandData();
    document.title = "Brand Data";
  }
}
</script>