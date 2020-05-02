<template>
  <div class="card card-description">
    <div class="row plain-element">
      <div class="col s10 m10 l10 plain-element">
          <div class="row plain-element left-align">
              <h3>{{ product.product_name}}</h3>
          </div>
          <div class="row row-functions left-align">
                            <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + product.clean_brand + '.png'"
                   class="img responsive img-icon">
          </div>
          <div v-if="product" class="row plain-element left-align">
              <h6>Category: </h6>
              <p>{{ product.product_category| truncatechars(1000)}}</p>
          </div>
          <div class="row plain-element left-align">
              <h6>Product Codes: </h6>
              <p>{{ product.product_code| truncatechars(1000)}}</p>
          </div>
          <div class="row plain-element left-align">
              <h6>Product Series: </h6>
              <p>{{ product.product_series| truncatechars(1000)}}</p>
          </div>
          <div class="row plain-element left-align">
              <h6>Part Number: </h6>
              <p>{{ product.product_part_number| truncatechars(1000)}}</p>
          </div>
          <div class="row plain-element left-align">
              <h6>Business:  </h6>
              <p>{{ product.business| truncatechars(1000)}}</p>
          </div>
          <div v-if="documentList" class="row plain-element documentation left-align">
              <h6>Documentation:  </h6>
              <div class="row plain-element" v-for="(element, index) in documentList" :key="index">
                <a target="_blank" :href="'https://johnsoncontrols.fluidtopics.net' + element.document_link">
                  <i class="fas fa-caret-right"></i> {{ element.document_title }}
                </a>
              </div>
          </div>
      </div>
      <div class="col s2 m2 l2 plain-element left-align col-product-images">
          <div class="row plain-element left-align">
              <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + randomInteger() + '.jpg'" class="img responsive img-description">
          </div>
          <br>
          <div class="row plain-element left-align">
              <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + randomInteger() + '.jpg'" class="img responsive img-description">
          </div>
          <div class="row plain-element left-align">
              <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + randomInteger() + '.jpg'" class="img responsive img-description">
          </div>
          <div class="row plain-element left-align">
              <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + randomInteger() + '.jpg'" class="img responsive img-description">
          </div>
          <div class="row plain-element left-align">
              <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/products/sample' + randomInteger() + '.jpg'" class="img responsive img-description">
          </div>
      </div>
  </div>
  </div>

</template>

<script>

export default {
  name: "ProductComponent",
   props: {
    product: {
      type: Object,
      required: true,
    },
    documentList: {
      type: Array,
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
      randomInteger() {
      return Math.floor(Math.random() * (15 - 1 + 1)) + 1;
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
  computed: {
//  Standard filter for topic list
    filteredTopicList() {
      return this.documentSortedTopics.filter(topics => {
        return topics.topic_title.toLowerCase().includes(this.search.toLowerCase())
      })
    },
  },
}

</script>
