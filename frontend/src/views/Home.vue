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
        <div v-if="error" class="plain-element">
          <div id="formError" class="row row-error text-center">
            <p class="error" v-if="error">{{ error }}</p>
            <p v-show="loadingDocuments">...loading...</p>
          </div>
        </div>
        <div v-if="documentList" class="plain-element">
          <DocumentListComponent
                  :documentList=documentList
                  :resultCount=resultCount
                  :next=next
          />
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import SidebarComponent from "@/components/SidebarComponent.vue"
import DocumentListComponent from "@/components/DocumentListComponent.vue"


export default {
  name: 'home',
  components: {
    SidebarComponent,
    DocumentListComponent,
  },
  data() {
    return {
        error: null,
        resultCount: null,
        search: "",
        searchQuery: null,
        next: null,
        documentList: null,
        loadingDocuments: false,
        currentSearch: "",
    }
  },
  methods: {
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
  created() {
    document.title = "Tech Comms";
  }
}


</script>
