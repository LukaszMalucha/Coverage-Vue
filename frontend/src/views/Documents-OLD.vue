<template>

<div id="page-index">
<div class="dashboard-cards">
        <div class="row row-search">
          <h4> Document Search</h4>
          <div class="row searchbox-wrapper">
            <form @submit.prevent="onSubmit">
              <input class="form-control" id="searchbox" type="text" placeholder="Search for Document"
                     aria-label="Search for Document" v-model="searchQuery">
                <button class="btn-transparent" type="submit"><i class="fas fa-search search-icon"></i></button>
            </form>
            <div id="formError" class="row row-error text-center">
                <p class="error" v-if="error">{{ error }}</p>
                <p v-show="loadingDocuments">...loading...</p>
            </div>
          </div>
        </div>
        <div class="row row-cards">
          <div class="row plain-element">
            <div class="col s1 m4 l4 col-results plain-element text-left">
                <p class="resultCount" v-if="resultCount">{{ resultCount }}</p>
            </div>
            <div class="col s10 m4 l4 plain-element">
              <div id="tableSearch" class="search-wrapper">
                <input type="text" placeholder="Keyword Search" class="place-holder-center" v-model="search"/>
              </div>
            </div>
            <div class="col s1 m4 l4 plain-element text-right">

              <button v-show="next" @click="onSubmit" class="btn btn-loading">
              Load More
              </button>
            </div>
          </div>
          <table id="dataTable">
             <thead>
                <tr v-if="filteredDocumentList.length > 0" class="table-header">
                  <th onclick="sortTable(0)" class="text-left field-long">Title</th>
                  <th onclick="sortTable(1)" class="text-center">Document Number</th>
                  <th onclick="sortTable(2)" class="text-center">Version</th>
                  <th onclick="sortTable(3)" class="text-center">Revison</th>
                  <th onclick="sortTable(4)" class="text-center">Type</th>
                  <th onclick="sortTable(5)" class="text-center">Created At</th>
                  <th onclick="sortTable(6)" class="text-center">Last Edition</th>
                  <th onclick="sortTable(7)" class="text-center">Last Publication</th>
                  <th onclick="sortTable(8)" class="text-center">Document</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="document in filteredDocumentList" :key="document.id">
                  <td class="text-left field-long">{{ document.document_title }}</td>
                  <td class="text-center field-medium">{{ document.document_number }}</td>
                  <td class="text-center field-short">{{ document.document_version }}</td>
                  <td class="text-center field-short">{{ document.document_revision }}</td>
                  <td class="text-center field-medium">{{ document.document_type }}</td>
                  <td class="text-center field-short">{{ document.document_created_at }}</td>
                  <td class="text-center field-short">{{ document.document_last_edition}}</td>
                  <td class="text-center field-short">{{ document.document_last_publication }}</td>
                  <td class="text-center field-short">
                    <a target="_blank" :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                        <i class="fas fa-file-pdf fa-2x"></i>
                    </a>
                  </td>
                </tr>
            </tbody>
          </table>
        </div>
      </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Documents",
  components: {

  },
  data() {
    return {
        error: null,
        resultCount: null,
        search: "",
        searchQuery: null,
        next: null,
        documentList: [],
        loadingDocuments: false,
        currentSearch: "",
    }
  },
  methods: {
    onSubmit() {
        this.resultCount = null;
        this.search = "";
        if (!this.searchQuery) {
            this.error = "Search Field can't be empty";
            setTimeout(() => this.error = null, 3000);
        } else {
           if (this.searchQuery != this.currentSearch) {
              this.documentList = [];
              this.next = null;
           }
           if (this.next) {
              endpoint = this.next;
           }

           let endpoint = `/api/documents/?search=${this.searchQuery}`;
           if (this.next) {
              endpoint = this.next;
           }
           this.loadingDocuments = true;
           apiService(endpoint)
            .then(data =>{
                if (data) {
                     this.resultCount = null;
                     this.loadingDocuments = false;
                     this.error = null;
                     window.console.log(data);
                     this.documentList.push(...data.results);
                     this.resultCount = data.count + " Results"
                     document.getElementById("tableSearch").style.display = "inline-table"
                     document.getElementById("dataTable").style.display = "inline-table"
                     if(data.next) {
                        this.next = data.next;
                        } else {
                          this.next = null;
                        }
                     this.currentSearch = this.searchQuery;
                } else {
                    this.error = "No document has been found"
                }
            })
        }
    }
  },
  computed: {
    filteredDocumentList() {
      return this.documentList.filter(document => {
        return document.document_title.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_number.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_version.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_revision.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_type.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_created_at.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_last_edition.toLowerCase().includes(this.search.toLowerCase()) ||
               document.document_last_publication.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    document.title = "Document Search";
  }
}


</script>