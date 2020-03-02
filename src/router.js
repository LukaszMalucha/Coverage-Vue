import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Companies from "./views/Brands.vue";
import BrandDetails from "./views/BrandDetails.vue";
import Documents from "./views/Documents.vue";
import QRGen from "./views/QRGen.vue";

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/brands",
      name: "brands",
      component: Companies
    },
    {
      path: "/brands/:brand",
      name: "brand-details",
      component: BrandDetails,
      props: true,
    },
    {
      path: "/qrgen",
      name: "qrgen",
      component: QRGen,
    },
    {
      path: "/documents",
      name: "documents",
      component: Documents
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
