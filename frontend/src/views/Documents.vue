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
            <div class="row row-documents">
                <div class="row plain-element">
                    <div class="col s1 m4 l4 col-results plain-element text-left">
                        <p class="resultCount" v-if="resultCount">{{ resultCount }}</p>
                    </div>
                    <div class="col s10 m4 l4 plain-element">
                        <div id="tableSearch" class="search-wrapper">
                            <input type="text" placeholder="Keyword Search" class="place-holder-center"
                                   v-model="search"/>
                        </div>
                    </div>
                    <div class="col s1 m4 l4 plain-element text-right">
                        <button v-show="next" @click="onSubmit" class="btn btn-loading">
                            Load More
                        </button>
                    </div>
                </div>
                <div v-for="document in filteredDocumentList" :key="document.id" class="row plain-element">

                    <div class="row plain-element row-document">
                        <div class="col s1 m1 l1 plain-element text-left col-image">
                            <img :src="'/static/img/brands/' + document.clean_brand + '.png'"  class="img img-document">
                        </div>
                        <div class="col s9 m9 l9 plain-element text-left">
                            <div class="row row-meta-top">
                                <h6>{{ document.document_title }}
                                </h6>
                                <p>{{ document.product.product_name }} </p>
                            </div>
                            <div class="row row-meta-bottom">
                                <div class="col s3 m3 l3 plain-element text-left">
                                    <p><i class="far fa-file-alt"></i> &nbsp; {{ document.document_number}}</p>
                                </div>

                                <div class="col s3 m3 l3 plain-element text-left">
                                    <p><i class="far fa-calendar-plus"></i> &nbsp; {{ document.document_created_at }}</p>
                                </div>
                                <div class="col s3 m3 l3 plain-element text-left">
                                    <p><i class="fas fa-edit"></i> &nbsp; {{ document.document_last_edition}}</p>
                                </div>
                                <div class="col s3 m3 l3 plain-element text-left">
                                    <p><i class="fas fa-paragraph"></i> &nbsp; {{ document.topics.length }} Topics</p>
                                </div>
                            </div>
                        </div>
                        <div class="col s2 m2 l2 plain-element text-left">
                            <a target="_blank" class="btn-quicklook" :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                                <i class="fas fa-eye"></i> Quick Look
                            </a>
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
                     this.resultCount = data.count + " Results";
                     document.getElementById("tableSearch").style.display = "inline-table";
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
               document.document_last_publication.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product.product_brand.toLowerCase().includes(this.search.toLowerCase())
      })
    },

  },
  created() {
    document.title = "Document Search";
  }
}


</script>