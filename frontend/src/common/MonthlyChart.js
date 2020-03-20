import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Bar,
  mixins: [reactiveProp],
  data(){
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
                  zeroLineColor: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                fontSize: 12
              }
          }],
          yAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
                  zeroLineColor: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                fontSize: 10,
                stepSize: 300,
                suggestedMin: 0,
              }
          }],

        },
        legend: {
          display: false
        },
        tooltips: {
          enabled: true,
          callbacks: {
            label: function(tooltipItem,data) {
              return data['datasets'][0]['data'][tooltipItem['index']] + " Documents";
            },
          }
        }
      }
    }
  },
  mounted () {
    this.renderChart(
      this.chartData,
      this.options
      )
  }
}