import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Companies from "./views/Brands.vue";
import Products from "./views/Products.vue";
import ProjectDetails from "./views/ProductDetails.vue";
import Documents from "./views/Documents.vue";
import DocumentDetails from "./views/DocumentDetails.vue";
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
      component: Products,
      props: true,
    },
    {
      path: "/product/:id",
      name: "product-details",
      component: ProjectDetails,
      props: true
    },
    {
      path: "/qrgen",
      name: "qrgen",
      component: QRGen,
    },
    {
      path: "/documents",
      name: "documents",
      component: Documents,
      props: true
    },
    {
      path: "/document/:id",
      name: "document-details",
      component: DocumentDetails,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
