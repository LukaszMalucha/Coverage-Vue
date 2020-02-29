<template>
<div id="page-index">
    <div class="row header">
        <div class="row top-menu">
            <div class="col-xs-8 col-sm-8 col-md-8 plain-element text-left">
            </div>
        </div>
    </div>
    <div class="dashboard-cards">
        <div class="row row-break"></div>
        <div class="row row-cards">
            <div class="col-md-2 plain-element"></div>
            <div class="col-md-4 plain-element">
            <router-link :to="{ name: 'brands'}">
                <div class="card menu-card">
                    <div class="card-image"><img
                            src="@/img/jc-grey.png"
                            class="img responsive">
                    </div>
                      <button class="btn btn-menu-card">
                        Brand Search
                      </button>
                  </div>
                  </router-link>
            </div>
            <div class="col-md-4 plain-element">
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
            <div class="col-md-2 plain-element"></div>
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
