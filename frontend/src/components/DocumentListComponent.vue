<template>
  <div class="row row-documents">
    <div class="row plain-element row-table-functions">
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

    <div v-for="document in filteredDocumentList" :key="document.id" class="row plain-element">
      <div class="row row-document">
        <div class="col s12 m10 l12 plain-element left-align">
          <div class="row row-meta-top">
            <router-link :to="{ name: 'document-details', params: {id: document.id, stringQuery: searchQuery}}">
              <div class="col s10 m9 l12 plain-element left-align col-meta-title">
                <h6>{{ document.document_title| truncatechars(240) }} </h6>
              </div>
            </router-link>
          </div>
          <router-link :to="{ name: 'document-details', params: {id: document.id, stringQuery: searchQuery}}">
            <div class="row row-meta-bottom">
              <div class="col s2 m2 l2 plain-element col-image">
                <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + document.clean_brand + '.png'"
                     class="img img-document">
              </div>
              <div class="col s6 m3 l3 plain-element left-align">
                <p>
                  <i v-if="getFileType(document.document_link) == 'viewer'" class="far fa-file-pdf"></i>
                  <i v-else class="far fa-file-alt"></i>
                  &nbsp; {{ document.document_number| truncatechars(30) }}
                </p>
              </div>
              <div class="col s6 m3 l3 plain-element left-align">
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
  </div>
</template>

<script>

export default {
  name: "DocumentListComponent",
  props: {
    documentList: {
      type: Array,
      required: true,
    },
    resultCount: {
      type: Number,
      required: false,
    },
    next: {
      type: Boolean,
      required: false,
    }
  },
  data() {
    return {
        error: null,
        search: "",
        searchQuery: null,
        loadingDocuments: false,
        currentSearch: "",
    }
  },
  methods: {
    getFileType(link) {
      return link.split("/")[1]

    },
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
               document.document_link.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product.product_brand.toLowerCase().includes(this.search.toLowerCase()) ||
               document.product.product_name.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  filters: {
      truncatechars (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
}

</script>