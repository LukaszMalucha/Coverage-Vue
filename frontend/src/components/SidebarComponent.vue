<template>
 <div class="col sidebar">
      <div class="row section">
        <div class="row">
          <span class="section-header">Search Engine</span>
        </div>
        <div  class="row">
        <router-link :to="{ name: 'home'}">
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-file fas-category"></i>Document Search</span>
            </div>
         </router-link>
        </div>
        <div  class="row">
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-cubes fas-category"></i>Product Search</span>
            </div>
        </div>

        <br>
        <div class="row">
          <span class="section-header">DB Manager</span>
        </div>
        <div  class="row">
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-database fas-category"></i>Product Upload </span>
            </div>
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-database fas-category"></i>Document Upload </span>
            </div>
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-database fas-category"></i>Topic Upload</span>
            </div>
        </div>
        <br>
        <div class="row">
          <span class="section-header">Admin</span>
        </div>
        <div  class="row">
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-users-cog fas-category"></i>Admin Panel</span>
            </div>
        </div>
        <div  class="row">
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-terminal fas-category"></i>REST API </span>
            </div>
        </div>
        <div  class="row">
            <div class="card menu-card">
              <span class="section-element"><i class="fas fa-caret-right"></i><i class="fas fa-chart-bar fas-category"></i>Analytics </span>
            </div>
        </div>
      </div>
    </div>
</template>

<script>

export default {
  name: "SidebarComponent",
}

</script>