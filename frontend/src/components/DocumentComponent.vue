<template>

  <div class="card card-description">
    <div class="row plain-element">
      <div class="col s12 m12 l12 plain-element">
        <div class="row plain-element left-align"><h3>{{ document.document_title }}</h3>

        </div>
        <div class="row row-functions row-functions-long left-align">
         <div class="col s12 m12 l9 plain-element">
           <div>
            <router-link v-if="document.clean_brand"   :to="{ name: 'brand-details', params: {brand: document.clean_brand}}">
                  <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + document.clean_brand + '.png'"
                       class="img responsive img-icon">
                </router-link>
                <router-link v-if="product_id" :to="{ name: 'product-details', params: {id: product_id}}">
                  <span class="product-name"> {{ product_name | truncatechars(240) }}</span>
                </router-link>
            </div>
         </div>
         <div class="col s12 m12 l3 plain-element right-align">
           <a v-if="document_link == 'viewer'" target="_blank" class="btn btn-document"  :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                  <i class="fas fa-file-pdf"></i> &nbsp; Document in PDF
                </a>
                <a v-else class="btn btn-document" target="_blank" :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                  <i class="fas fa-file-code"></i> &nbsp; Document in HTML
                </a>
          </div>
        </div>
        <div class="row plain-element left-align">
          <div class="col s12 m12 l6 plain-element">
            <div class="row plain-element left-align">
                    <h6>Document Number: </h6>
                    <p>{{ document.document_number }}</p>
                  </div>
                  <div class="row plain-element left-align">
                    <h6>Document Version: </h6>
                    <p>{{ document.document_version }}</p>
                  </div>
                  <div class="row plain-element left-align">
                    <h6>Document Type: </h6>
                    <p>{{ document.document_type }}</p>
                  </div>
                  <div class="row plain-element left-align">
                    <h6>Date Created: </h6>
                    <p>{{ document.document_created_at}}</p>
                  </div>
                  <div class="row plain-element left-align">
                    <h6>Last Edition: </h6>
                    <p>{{ document.document_last_edition }}</p>
                  </div>
                  <div class="row plain-element left-align">
                    <h6>Last Publication: </h6>
                    <p>{{ document.document_last_publication }}</p>
                  </div>
          </div>
          <div class="col s12 m12 l6 plain-element col-topics">
            <div class="row plain-element left-align">
              <h6>Document Content:</h6>
            </div>
            <div class="row plain-element left-align">
              <div class="col s4 m4 l5 plain-element left-align filter-wrapper">
                <input id="contentFilter" type="text" placeholder="Content Filter" v-model="search">
              </div>
            </div>
            <div v-for="element in filteredTopicList" class="row plain-element left-align" :key="element.id">
              <div v-if="element.topic_depth == 2" class="row plain-element left-align">
                <li>
                  <a class="topic-tier-2" target="_blank"
                     :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                    {{element.topic_title| truncatechars(240)}}
                  </a>
                </li>
              </div>
              <div v-else-if="element.topic_depth == 3" class="row plain-element left-align">
                <ol>
                  <a class="topic-tier-3" target="_blank"
                     :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                    &#9656; {{element.topic_title| truncatechars(240)}}
                  </a>
                </ol>
              </div>
              <div v-else-if="element.topic_depth == 4" class="row plain-element left-align">
                <ol>
                  <a class="topic-tier-4" target="_blank"
                     :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                    &#9656; {{element.topic_title| truncatechars(240)}}
                  </a>
                </ol>
              </div>
              <div v-else class="row plain-element left-align">
                <ol>
                  <a v-bind:style="{
                                    'margin-left': (element.topic_depth * 6) + 'px',
                                    'font-size': (14 - (element.topic_depth * 0.25)) + 'px',
                                    'color':  '#66' + element.topic_depth + element.topic_depth + element.topic_depth + element.topic_depth,
                                    }" class="topic-other"
                     target="_blank" :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                    {{element.topic_title| truncatechars(240)}}
                  </a>
                </ol>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

export default {
  name: "DocumentComponent",
   props: {
    document: {
      type: Object,
      required: true,
    },
    documentSortedTopics: {
      type: Array,
      required: true,
    },
    product_id: {
      type: String,
      required: true,
    },
    product_name: {
      type: String,
      required: true,
    },
    document_link: {
      type: String,
      required: true,
    }

  },
  data() {
    return {
      search: "",
    }
  },
  methods: {
//  Function for sorting document topics
      sortArrays(arrays) {
              return _.orderBy(arrays, 'topic_breadcrumb');
      },
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
  computed: {
//  Standard filter for topic list
    filteredTopicList() {
      return this.documentSortedTopics.filter(topics => {
        return topics.topic_title.toLowerCase().includes(this.search.toLowerCase())
      })
    },
//  Function that retrieve viewer/reader from document link
    getFileType() {
      return  this.document.document_link.split("/")[1]

    },
  },
}

</script>

 :document = document
:product_id = product_id.toString()
:product_name = product_name
:document_link = document_link