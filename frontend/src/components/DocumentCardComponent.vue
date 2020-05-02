<template>
<div v-if="index%2 == 0"  class="row row-document ">
    <div class="col s1 m1 l1 plain-element col-image">
      <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + doc.clean_brand + '.png'"
           class="img img-document">
    </div>
    <div class="col s9 m9 l9 left-align">
      <h6>{{ doc.document_title| truncatechars(240) }}</h6>
    </div>
</div>
<div v-else  class="row row-document-2">
  <div class="col s1 m1 l1 plain-element col-image">
      <img :src="'https://techcomms.s3-eu-west-1.amazonaws.com/static/img/brands/' + doc.clean_brand + '.png'"
           class="img img-document">
  </div>
  <div class="col s9 m9 l9 left-align">
    <h6>{{ doc.document_title| truncatechars(240) }}</h6>
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
    index: {
      type: Number,
      required: true,
    }
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