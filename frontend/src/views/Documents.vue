<template>
  <div id="page-index">
    <div class="row header">
      <div class="row searchbox-wrapper searchbox-long">
        <form @submit.prevent="submitQuery">
          <input class="form-control" id="searchbox" type="text" placeholder="Search for Document"
                 aria-label="Search for Document" v-model="searchQuery">
          <button class="btn-transparent" type="submit"><i class="fas fa-search search-icon"></i></button>
        </form>
      </div>
    </div>
    <div class="dashboard-cards">
      <div id="formError" class="row row-error text-center">
          <p class="error" v-if="error">{{ error }}</p>
          <p v-show="loadingDocuments">...loading...</p>
      </div>
      <div class="row row-documents">
        <div class="row plain-element row-table-functions">
          <div class="col s1 m3 l4 col-results plain-element left-align">
            <p class="resultCount" v-if="resultCount && filteredDocumentList.length > 0">{{ resultCount }}</p>
          </div>
          <div class="col s9 m6 l4 plain-element">
            <div v-if="documentList.length > 0" id="tableSearch" class="filter-wrapper">
              <input type="text" placeholder="Keyword Filter" class="place-holder-center"
                     v-model="search"/>
            </div>
          </div>
          <div class="col s3 m3 l4 plain-element right-align">
            <button v-if="resultCount && filteredDocumentList.length > 0" v-show="next" @click="submitQuery"
                    class="btn btn-loading">
              Load More
            </button>
          </div>
        </div>
        <div v-for="document in filteredDocumentList" :key="document.id" class="row plain-element">

          <div class="row plain-element row-document">
            <div class="col s2 m2 l1 plain-element col-image">
              <img :src="'/static/img/brands/' + document.clean_brand + '.png'" class="img img-document">
            </div>

            <div class="col s12 m10 l11 plain-element left-align">
              <div class="row row-meta-top">
                <router-link :to="{ name: 'document-details', params: {id: document.id, stringQuery: searchQuery}}">
                  <div class="col s10 m9 l10 plain-element left-align col-meta-title">
                    <h6>{{ document.document_title| truncatechars(240) }} </h6>
                  </div>
                </router-link>
                <div class="col s12 m3 l2 plain-element left-align">
                  <a target="_blank" class="btn-quicklook"
                     :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                    <i class="fas fa-eye"></i> Quick Look
                  </a>
                </div>
              </div>
              <router-link :to="{ name: 'document-details', params: {id: document.id, stringQuery: searchQuery}}">
                <div class="row row-meta-bottom">
                  <div class="col s6 m3 l2 plain-element left-align">
                    <p>
                      <i v-if="getFileType(document.document_link) == 'viewer'" class="far fa-file-pdf"></i>
                      <i v-else class="far fa-file-alt"></i>
                      &nbsp; {{ document.document_number| truncatechars(30) }}
                    </p>
                  </div>
                  <div class="col s6 m3 l2 plain-element left-align">
                    <p><i class="far fa-calendar-plus"></i> &nbsp; {{ document.document_created_at }}</p>
                  </div>
                  <div class="col s6 m3 l2 plain-element left-align">
                    <p><i class="fas fa-edit"></i> &nbsp; {{ document.document_last_edition}}</p>
                  </div>
                  <div class="col s6 m3 l2 plain-element left-align">
                    <p><i class="far fa-bookmark"></i> &nbsp; {{ document.topics.length }} Topics</p>
                  </div>
                  <div class="col s12 m12 l4 plain-element left-align">
                    <p><i class="fas fa-cube"></i> &nbsp; {{ document.product.product_name| truncatechars(48) }}</p>
                  </div>
                </div>
              </router-link>
            </div>
          </div>

        </div>
        <br>
        <div v-if="resultCount && filteredDocumentList.length > 0" class="row plain-element">
          <button v-show="next" @click="submitQuery" class="btn btn-loading">
            Load More
          </button>
        </div>
        <div v-if="resultCount && filteredDocumentList.length == 0" class="row plain-element">
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
    props: {
//    Only needed if this website is being accessed from product details page in order to get product documentation
      productId: {
        type: String,
        required: false,
      },
      stringQuery: {
        type: String,
        required: false,
      }
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
//  Query documents database
    submitQuery() {
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
    },
//  Function that retrieve viewer/reader from document link
    getFileType(link) {
      return link.split("/")[1]

    }
  },
  computed: {
//  Function that filters list of documents
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
               document.document_link.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product.product_brand.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product.product_name.toLowerCase().includes(this.search.toLowerCase())
      })
    }
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
    document.title = "Document Search";
//   In case of being redirected from product details page in order to find product documentation
    if (this.productId) {
      this.searchQuery = this.productId;
      this.submitQuery();
      window.console.log(this.searchQuery);
      this.searchQuery = null;
    }
  }
}



</script>