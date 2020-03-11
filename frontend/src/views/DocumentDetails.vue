<template>
  <div id="page-index">
    <div class="dashboard-cards">
      <div class="row row-break"></div>
      <div class="row row-cards">
        <div class="card card-description">
          <div class="row plain-element left-align row-back">
            <router-link :to="{ name: 'brand-details', params: {brand: document.clean_brand}}">
              <i class="fas fa-chevron-left"></i> Back To Search
            </router-link>
          </div>
          <br>
          <div class="row plain-element">
            <div class="col s6 m8 l12 plain-element">
              <div class="row plain-element left-align">
                <h3>{{ document.document_title}}</h3>
                <div>
                  <img style="vertical-align:middle" :src="'/static/img/brands/' + document.clean_brand + '.png'"
                       class="img responsive img-icon">
                  <span class="product-name">{{ product_name }}</span>
                </div>
              </div>
              <div class="row row-functions row-functions-long left-align">
                <a v-if="getFileType(document.document_link) == 'viewer'" target="_blank" class="btn btn-document"  :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                  <i class="fas fa-file-pdf"></i> &nbsp; Document in PDF
                </a>
                <a v-else class="btn btn-document" target="_blank" :href="'https://johnsoncontrols.fluidtopics.net' + document.document_link">
                  <i class="fas fa-file-code"></i> &nbsp; Document in HTML
                </a>
              </div>
              <div class="row plain-element left-align">
                <div class="col s12 m12 l6 plain-element">
                  <div class="row plain-element left-align">
                    <h4>Document Metadata:</h4>
                  </div>
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
                    <p>{{ document.document_version }}</p>
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
                <div v-if="documentTopics.length > 0" class="col s12 m12 l6 plain-element col-topics">
                  <div class="row plain-element left-align">
                    <h4>Document Topics:</h4>
                  </div>
                  <div class="row plain-element left-align">
                    <div class="col s4 m4 l3 plain-element left-align">
                      <input type="text" placeholder="Topic Filter" v-model="search"/>
                    </div>
                  </div>
                  <br>
                  <div v-for="element in filteredTopicList" class="row plain-element left-align" :key="element.id">
                    <div v-if="element.topic_depth == 2" class="row plain-element left-align">
                      <li>
                        <a class="topic-tier-2" target="_blank"
                           :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                          {{element.topic_title}}
                        </a>
                      </li>
                    </div>
                    <div v-else-if="element.topic_depth == 3" class="row plain-element left-align">
                      <ol>
                        <a class="topic-tier-3" target="_blank"
                           :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                          &#9656; {{element.topic_title}}
                        </a>
                      </ol>
                    </div>
                    <div v-else-if="element.topic_depth == 4" class="row plain-element left-align">
                      <ol>
                        <a class="topic-tier-4" target="_blank"
                           :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                          &#9656; {{element.topic_title}}
                        </a>
                      </ol>
                    </div>
                    <div v-else class="row plain-element left-align">
                      <ol>
                        <a v-bind:style="{
                                          'margin-left': (element.topic_depth * 15) + 'px',
                                          'font-size': (14 - (element.topic_depth * 0.25)) + 'px',
                                          'color':  '#66' + element.topic_depth + element.topic_depth + element.topic_depth + element.topic_depth,
                                          }" class="topic-other"
                           target="_blank" :href="'https://johnsoncontrols.fluidtopics.net' + element.topic_link">
                          {{element.topic_title}}
                        </a>
                      </ol>
                    </div>
                  </div>

                </div>
              </div>


            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import _ from 'lodash';

export default {
  name: "DocumentDetails",
  props: {
    id: {
      required: true
    }
  },
  data() {
    return {
      document: [],
      documentTopics: [],
      product_name: "",
      search: "",
    }
  },
  methods: {
//  Function for sorting document topics
    sortArrays(arrays) {
            return _.orderBy(arrays, 'topic_breadcrumb');
    },
//  Function for retrieving document data with given document.id
    getDocumentData() {
      let endpoint = `/api/documents/${this.id}/`;
      apiService(endpoint)
          .then(data => {
            window.console.log(endpoint);
            window.console.log(data);
            if (data) {
              this.document = data;
              this.product_name = this.document.product['product_name'];
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
    //  Function that retrieve viewer/reader from document link
    getFileType(link) {
      return link.split("/")[1]

    },
  },
  computed: {
//  Standard filter for topic list
    filteredTopicList() {
      return this.documentSortedTopics.filter(topics => {
        return topics.topic_title.toLowerCase().includes(this.search.toLowerCase())
      })
    },
  },
  created() {
    this.getDocumentData();
  }
}

</script>
