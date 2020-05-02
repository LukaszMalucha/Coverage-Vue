<template>
<div class="row row-document">
  <div class="col s12 m12 l12 plain-element left-align">
    <div class="row row-meta-top">
        <div class="col s12 m12 l12 plain-element left-align col-meta-title">
          <h6>{{ doc.document_title| truncatechars(240) }} </h6>
        </div>
    </div>
      <div class="row row-meta-bottom">
        <div class="col s2 m2 l2 plain-element col-image">
          <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + doc.clean_brand + '.png'"
               class="img img-document">
        </div>
        <div class="col s3 m3 l3 plain-element left-align">
          <p>
            <i v-if="getFileType(doc.document_link) == 'viewer'" class="far fa-file-pdf"></i>
            <i v-else class="far fa-file-alt"></i>
            &nbsp; {{ doc.document_number| truncatechars(30) }}
          </p>
        </div>
        <div class="col s3 m3 l3 plain-element left-align">
          <p><i class="far fa-bookmark"></i> &nbsp; {{ doc.topics.length }} Topics</p>
        </div>
        <div class="col s4 m4 l4 plain-element left-align">
          <p><i class="fas fa-cube"></i> &nbsp; {{ doc.product.product_name| truncatechars(42) }}</p>
        </div>
      </div>
  </div>
</div>
</template>

<script>

export default {
  name: "DocumentCardComponent",
  props: {
    doc: {
      type: Object,
      required: true,
    },
  },
  methods: {
    getFileType(link) {
      return link.split("/")[1]

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
}

</script>