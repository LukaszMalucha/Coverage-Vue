<template>
    <div id="page-index">
        <div class="row header">
            <div class="row searchbox-wrapper searchbox-long">
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

        <div class="dashboard-cards">
            <div class="row row-documents">
                <div class="row plain-element">
                    <div class="col s1 m3 l4 col-results plain-element left-align">
                        <p class="resultCount" v-if="resultCount && filteredDocumentList.length > 0">{{ resultCount }}</p>
                    </div>
                    <div class="col s9 m6 l4 plain-element">
                        <div id="tableSearch" class="filter-wrapper">
                            <input type="text" placeholder="Keyword Filter" class="place-holder-center"
                                   v-model="search"/>
                        </div>
                    </div>
                    <div class="col s3 m3 l4 plain-element right-align">
                        <button v-if="resultCount && filteredDocumentList.length > 0" v-show="next" @click="onSubmit" class="btn btn-loading">
                            Load More
                        </button>
                    </div>
                </div>
                <div v-for="document in filteredDocumentList" :key="document.id" class="row plain-element">
                  <router-link :to="{ name: 'document-details', params: {id: document.id}}">
                    <div class="row plain-element row-document">
                        <div class="col s2 m2 l1 plain-element col-image">
                            <img :src="'/static/img/brands/' + document.clean_brand + '.png'"  class="img img-document">
                        </div>
                        <div class="col s12 m10 l11 plain-element left-align">
                            <div class="row row-meta-top">
                              <div class="col s10 m9 l8 plain-element left-align">
                                  <h6>{{ document.document_title }}</h6>
                              </div>
                              <div class="col s12 m3 l4 plain-element left-align">
                                  <a target="_blank" class="btn-quicklook" :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                                      <i class="fas fa-eye"></i> Quick Look
                                  </a>
                              </div>
                            </div>
                            <div class="row row-meta-bottom">
                                <div class="col s6 m3 l2 plain-element left-align">
                                    <p><i class="far fa-file-alt"></i> &nbsp; {{ document.document_number}}</p>
                                </div>
                                <div class="col s6 m3 l2 plain-element left-align">
                                    <p><i class="far fa-calendar-plus"></i> &nbsp; {{ document.document_created_at }}</p>
                                </div>
                                <div class="col s6 m3 l2 plain-element left-align">
                                    <p><i class="fas fa-edit"></i> &nbsp; {{ document.document_last_edition}}</p>
                                </div>
                                <div class="col s6 m3 l2 plain-element left-align">
                                    <p><i class="far fa-bookmark"></i> &nbsp; {{ document.topic.length }} Topics</p>
                                </div>
                                <div class="col s12 m12 l4 plain-element left-align">
                                    <p><i class="fas fa-cube"></i> &nbsp; {{ document.product.product_name| truncatechars(48) }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                  </router-link>
                 </div>
                 <br>
                <div v-if="resultCount && filteredDocumentList.length > 0" class="row plain-element">
                   <button v-show="next" @click="onSubmit" class="btn btn-loading">
                            Load More
                    </button>
                </div>
                <div v-if="resultCount && filteredDocumentList.length == 0"   class="row plain-element">
                  <h6>No results match search criteria</h6>
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
               document.product.product_brand.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product.product_name.toLowerCase().includes(this.search.toLowerCase())
      })
    },

  },
  filters: {
      truncatechars (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
  created() {
    document.title = "Document Search";
  }
}


</script>