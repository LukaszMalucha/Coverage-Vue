<template>
<div class="col s12 m5 col-content plain-element">
  <div class="card card-description">
    <div class="row plain-element">
      <div class="col s6 m8 l12 plain-element">
        <div class="row plain-element left-align"><h3>{{ document.document_title }}</h3>

        </div>
        <div class="row row-functions row-functions-long left-align">
         <div class="col s6 m8 l6 plain-element">
           <div>
            <router-link v-if="document.clean_brand"   :to="{ name: 'brand-details', params: {brand: document.clean_brand}}">
                  <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + document.clean_brand + '.png'"
                       class="img responsive img-icon">
                </router-link>
                <router-link v-if="product_id" :to="{ name: 'product-details', params: {id: product_id}}">
                  <span class="product-name">{{ product_name | truncatechars(240) }}</span>
                </router-link>
            </div>
         </div>
         <div class="col s6 m8 l6 plain-element right-align">
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
              <p>TD-2058</p></div>
            <div class="row plain-element left-align"><h6>Document Version: </h6>
              <p>Not Specified</p></div>
            <div class="row plain-element left-align"><h6>Document Type: </h6>
              <p>User Guide</p>
            </div>
            <div class="row plain-element left-align">
              <h6>Date Created: </h6>
              <p>2003-12-31</p>
            </div>
            <div class="row plain-element left-align">
              <h6>Last Edition: </h6>
              <p>2003-12-31</p>
            </div>
            <div class="row plain-element left-align">
              <h6>Last Publication: </h6>
              <p>2003-12-31</p>
            </div>
          </div>
          <div class="col s12 m12 l6 plain-element col-topics">
            <div class="row plain-element left-align">
              <h6>Document Content:</h6>
            </div>
            <div class="row plain-element left-align">
              <div class="col s4 m4 l5 plain-element left-align filter-wrapper">
                <input id="contentFilter" type="text" placeholder="Content Filter">
              </div>
            </div>
            <div class="row plain-element left-align">
              <div class="row plain-element left-align">
                <li><a target="_blank"
                       href="https://johnsoncontrols.fluidtopics.net/reader/IdBsjc3W0aHJOz~IWP9GRQ/FmR~yUOikHQI4O6ndyfUJQ"
                       class="topic-tier-2"> Configuration </a></li>
              </div>
            </div>
            <div class="row plain-element left-align">
              <div class="row plain-element left-align">
                <ol><a target="_blank"
                       href="https://johnsoncontrols.fluidtopics.net/reader/IdBsjc3W0aHJOz~IWP9GRQ/NdHYvrLrd~vUbhdNg_kO6g"
                       class="topic-tier-3"> ▸ Camera connections </a></ol>
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

export default {
  name: "DocumentComponent",
   props: {
    document: {
      type: Object,
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
     filters: {
//  Just in case if some strings would be too long and would destroy a layout
      truncatechars (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
}

</script>