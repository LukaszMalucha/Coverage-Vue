<template>
 <div class="col sidebar">
      <div class="row section">
        <div class="row">
          <span class="section-header">Search Engine</span>
        </div>
        <div  class="row">
        <router-link :to="{ name: 'home'}">
            <div v-if="active == 'documents'" class="card menu-card active">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-file fas-category"></i>Document Search</span>
            </div>
            <div v-else class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-file fas-category"></i>Document Search</span>
            </div>
         </router-link>
        </div>
        <div  class="row">
          <router-link :to="{ name: 'products'}">
              <div v-if="active == 'products'" class="card menu-card active">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-cubes fas-category"></i>Product Search</span>
              </div>
              <div v-else class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-cubes fas-category"></i>Product Search</span>
              </div>
          </router-link>
        </div>
        <br>
        <div class="row">
          <span class="section-header">DB Manager</span>
        </div>
        <div  class="row">
            <a href="/db/products-upload">
              <div class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-database fas-category"></i>Product Upload </span>
              </div>
            </a>
            <a href="/db/documents-upload">
              <div class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-database fas-category"></i>Document Upload </span>
              </div>
            </a>
            <a href="/db/topics-upload">
              <div class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-database fas-category"></i>Topic Upload</span>
              </div>
            </a>
        </div>
        <br>
        <div class="row">
          <span class="section-header">Admin</span>
        </div>
        <div  class="row">
            <a href="/admin/">
              <div class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-users-cog fas-category"></i>Admin Panel</span>
              </div>
            </a>
        </div>
        <div  class="row">
            <a href="/api/">
              <div class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-terminal fas-category"></i>REST API </span>
              </div>
            </a>
        </div>
        <div  class="row">
            <a href="/analytics">
              <div class="card menu-card">
                <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-chart-bar fas-category"></i>Analytics </span>
              </div>
            </a>
        </div>
      </div>
    </div>
</template>

<script>

export default {
  name: "SidebarComponent",
  props: {
    active:{
      type: String,
      required:true,
    }
  },

}

</script>