<template>
<div id="page-index">
    <div class="row header">
        <div class="row top-menu">
            <div class="col s8 m8 l8 plain-element left-align">
            </div>
        </div>
    </div>
    <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-menu center-align ">
            <div class="col s12 m6 l6 plain-element">
            <router-link :to="{ name: 'brands'}">
                <div class="card menu-card">
                    <div class="card-image"><img
                            src="@/img/jc-grey.png"
                            class="img responsive">
                    </div>
                      <button class="btn btn-menu-card">
                        Product Search
                      </button>
                  </div>
                  </router-link>
            </div>
            <div class="col s12 m6 l6 plain-element">
                <router-link :to="{ name: 'documents'}">
                    <div class="card menu-card">
                        <div class="card-image"><img
                                src="@/img/docs.jpg"
                                class="img responsive">
                        </div>
                        <router-link :to="{ name: 'documents'}">
                          <button class="btn btn-menu-card">
                            Document Search
                          </button>
                        </router-link>
                        </div>
                </router-link>
            </div>

        </div>
    </div>
</div>
</template>

<script>

export default {
  name: 'home',
  components: {
  },
  created() {
    document.title = "Tech Comms";
  }
};

</script>
