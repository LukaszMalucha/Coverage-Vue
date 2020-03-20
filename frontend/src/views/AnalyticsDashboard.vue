<template>
<div id="page-index">
  <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-cards">
            <div class="card card-description">
                <div v-if="dataList" class="col s12 m3 l3 plain-element left-align">
                  <div class="row plain-element">
                    <div v-if="brandData" class="card insights-card insights-card-narrow-left">
                      <div class="card-header"><img src="/static/img/logo.png" class="img-icon">
                        <p><b>TechComms Documentation</b> <br>Current Document & Product Count </p>
                      </div>
                      <div class="row-image">
                          <div class="table-responsive">
                              <table class="table table-content">
                                  <tbody>
                                    <tr>
                                        <td>Document Count</td>
                                        <td class="center">{{ documentCount }}</td>
                                    </tr>
                                    <tr>
                                        <td>Topic Count </td>
                                        <td class="center">{{ topicCount }}</td>
                                    </tr>
                                    <tr>
                                        <td>Product Count</td>
                                        <td class="center">{{ productCount }}</td>
                                    </tr>
                                  </tbody>
                              </table>
                          </div>
                      </div>
                    </div>
                  </div>
                  <div class="row plain-element">
                    <div v-if="brandData" class="card insights-card insights-card-narrow-left">
                      <div class="card-header"><img src="/static/img/logo.png" class="img-icon">
                      <p><b>TechComms Document Types</b> <br>Most Common Document Types </p></div>
                      <div class="row-image">
                          <div class="table-responsive">
                              <table class="table table-content">
                                  <tbody>
                                  <tr v-for="(key, value) in documentTypes" :key="value">
                                      <td>{{ value }}</td>
                                      <td class="center">{{ key }}</td>
                                  </tr>
                                  </tbody>
                              </table>
                          </div>
                       </div>
                  </div>
                    </div>
                </div>
                <div class="col s12 m6 l6 plain-element left-align">
                  <div v-if="monthlyChartData" class="row plain-element">
                    <div class="card insights-card insights-card-middle">
                      <div class="card-header"><img src="/static/img/logo.png" class="img-icon"><p><b>Linkedin Analytics</b> <br>IT Companies </p></div>
                    </div>
                    <div class="chart">
                      <monthly-chart  :chart-data="monthlyChartData" :styles="chartStyles"> </monthly-chart>
                    </div>
                   </div>

                  <div class="row plain-element">
                    <div  v-if="weeklyChartData" class="card insights-card insights-card-middle">
                      <div class="card-header"><img src="/static/img/logo.png" class="img-icon"><p><b>Linkedin Analytics</b> <br>IT Companies </p></div>
                    </div>
                    <div class="chart">
                      <weekly-chart  :chart-data="weeklyChartData" :styles="chartStyles"> </weekly-chart>
                    </div>
                  </div>
                </div>
                <div class="col s12 m3 l3 plain-element left-align">
                  <div class="row plain-element">
                    <div v-if="brandData" class="card insights-card insights-card-narrow-right">
                      <div class="card-header"><img src="/static/img/logo.png" class="img-icon"><p><b>Linkedin Analytics</b> <br>IT Companies </p></div>
                      <div class="row-image">
                          <div class="table-responsive">
                              <table class="table table-content" id="tableEstablished">
                                  <tbody>

                                  <tr v-for="(key, value) in brandData" :key="value">
                                      <td>{{ value }}</td>
                                      <td class="center">{{ key }}</td>
                                  </tr>

                                  </tbody>
                              </table>
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
import MonthlyChart from "@/common/MonthlyChart.js";
import WeeklyChart from "@/common/WeeklyChart.js";

export default {
  name: "AnalyticsDashboard",
  components: {
    MonthlyChart,
    WeeklyChart,

  },
  data() {
    return {
        dataList: [],
        monthlyChartData: {},
        weeklyChartData: {},
        brandData: {},
        mostTopics: {},
        documentTypes: {},
        documentCount: null,
        topicCount: null,
        productCount: null,
    }
  },
  methods: {
//  Method that makes API call and retrieve an analytics data
    getAnalyticsData() {
    let endpoint = "/api/analytics/dashboard";
    apiService(endpoint)
        .then(data => {
            if (data) {
              this.dataList = data;
              this.monthlyChartData = data.month_count_dict;
              this.weeklyChartData = data.day_of_the_week_count_dict;
              this.weeklyChartData = data.day_of_the_week_count_dict;
              this.brandData = data.brand_count_dict;
              this.documentCount = data.document_count;
              this.topicCount = data.topic_count;
              this.productCount = data.product_count;
              this.documentTypes = data.document_type_count_dict;
              this.mostTopics = data.most_topics_per_document_dict;
              window.console.log(this.dataList);
              this.fillMonthlyChart();
              this.fillWeeklyChart();
            } else {
                this.dataList = [];
                document.title = "404 - Not Found"
            }
        })
    },
    fillMonthlyChart() {
      var dataset = this.monthlyChartData
      var dataLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
      var dataValues = Object.values(dataset)
      this.monthlyChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", "#f28e2b"],
            data: dataValues
          }
        ]
      }
    },
    fillWeeklyChart() {
      var dataset = this.weeklyChartData
      var dataLabels = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat" ]
      var dataValues = Object.values(dataset)
      this.weeklyChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", "#f28e2b"],
            data: dataValues
          }
        ]
      }
    },

  },
  computed: {
    chartStyles () {
      return {
        height: `100%`,
        position: "relative"
      }
    }
  },
  created() {
    document.title = "TechComms Analytics";
    this.getAnalyticsData();
  }
}
</script>
