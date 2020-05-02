import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Products from "./views/Products.vue";
import AnalyticsDashboard from "./views/AnalyticsDashboard.vue"

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
      path: "/products",
      name: "products",
      component: Products,
    },
    {
      path: "/analytics",
      name: "analytics",
      component: AnalyticsDashboard,
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
