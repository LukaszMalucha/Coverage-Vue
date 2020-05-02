<template>
<div id="page-index">
  <div class="row plain-element">
    <SidebarComponent/>
    <div class="col s12 m5 col-content plain-element">
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
        <div class="row row-documents" >
          <div class="row row-table-functions" >
            <div class="col s1 m3 l4 col-results plain-element left-align">
              <p class="resultCount" v-if="resultCount && filteredDocumentList.length > 0">{{ resultCount }}</p>
              <button v-if="resultCount && filteredDocumentList.length > 0" @click="csvExport()" class="btn btn-export">
                <i class="fas fa-file-download"></i>
              </button>
            </div>
            <div class="col s9 m6 l4 plain-element">
              <div v-if="documentList.length > 0" id="tableSearch" class="filter-wrapper">
                <input id="keywordFilter" type="text" placeholder="Keyword Filter" class="place-holder-center"
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
          <div id="parent">
            <div id="child">
              <div v-for="(doc, index) in filteredDocumentList" :key="index" class="row plain-element">
                <a @click="getDocumentData(doc.id)">
                    <DocumentCardComponent
                      :doc = doc
                      :index = index
                    />
                </a>
              </div>
             <div v-if="documentList.length > 0" class="border-line"></div>
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
    <div class="col s12 m5 col-content-right plain-element" style="border-right: none;">
      <div v-if="document" class="plain-element">
        <DocumentComponent
          :document = document
          :product_id = product_id.toString()
          :product_name = product_name
          :document_link = document_link
          :documentSortedTopics = documentSortedTopics
        />
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import SidebarComponent from "@/components/SidebarComponent.vue";
import DocumentComponent from "@/components/DocumentComponent.vue";
import DocumentCardComponent from "@/components/DocumentCardComponent.vue";
import _ from 'lodash';


export default {
  name: 'home',
  components: {
    SidebarComponent,
    DocumentComponent,
    DocumentCardComponent,
  },
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
        document: null,
        documentTopics: [],
        document_link: "",
        product_name: "",
        product_id: "",
    }
  },
  methods: {
    sortArrays(arrays) {
      return _.orderBy(arrays, 'topic_breadcrumb');
    },
    getDocumentData(documendId) {
      let endpoint = `/api/documents/${documendId}/`;
      apiService(endpoint)
          .then(data => {
            window.console.log(endpoint);
            window.console.log(data);
            if (data) {
              this.document = data;
              this.product_id = this.document.product['id'];
              this.product_name = this.document.product['product_name'];
              this.document_link = this.document.document_link.split("/")[1]
              this.documentTopics = this.document.topics;
              this.documentSortedTopics = this.sortArrays(this.documentTopics);
              window.console.log(this.documentSortedTopics);
              document.title = this.document.document_title;
            } else {
              this.document = null;
              document.title = "404 - Page Not Found"
            }
          })
    },
//  Function that exports current query to txt
    csvExport() {
      let csvContent = "data:text/csv;charset=utf-8,";
      var responseData = this.documentList;
      const header = ["document_title;document_number;document_part_number;document_version;document_revision;document_type;document_created_at;document_last_edition;document_last_publication;document_revised_modified;document_brand;document_link"]
      const products = responseData.map(x => ([x.document_title,
                                               x.document_number,
                                               x.document_part_number,
                                               x.document_version,
                                               x.document_revision,
                                               x.document_type,
                                               x.document_created_at,
                                               x.document_last_edition,
                                               x.document_last_publication,
                                               x.document_revised_modified,
                                               x.document_brand,
                                               x.document_link,
                                                ]).join(";"));
      csvContent += header.join("\n");
      csvContent += ("\n")
      csvContent += products.join("\n");
      const queryData = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", queryData);
      link.setAttribute("download", "export.txt");
      link.click();
    },

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
    document.title = "Tech Comms";
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
