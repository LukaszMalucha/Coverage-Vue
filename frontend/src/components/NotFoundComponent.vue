<template>
<div class="row plain-element">
  <div id="errorContainer">
    <div id="mainContainer">
      <div class="company"><img src="https://techcomms.s3-eu-west-1.amazonaws.com/static/img/logo-404.png" width="290" height="140"
                             alt="Logo"/></div>
      <br clear="all"/>

      <div class="robot"><img src="https://techcomms.s3-eu-west-1.amazonaws.com/static/img/404.png" width="380" height="450" alt="Robot 404"/></div>

      <div class="error-header"><span class="largeFont">Oops!</span> The Page you requested was not found</div>
      <br clear="right"/>

      <div class="mainContent">
          <p class="p-error">HTTP 404 Error - The page you are looking for appears <br> to have been moved, deleted or does not exist</p>

          <p class="p-error"><strong>You can try:</strong></p>
          <ul class="ul-error">
              <li>&#8226; Visit the <a href="/">Homepage</a>
              </li>
              <li>&#8226; Make sure that the address is spelled correctly</li>
              <li>&#8226; Go to <a href="javascript:history.go(-1);">previous</a> page
              </li>
          </ul>
      </div>
    </div>
  </div>
</div>
</template>

<script>

export default {
  name: "NotFoundComponent",
}
</script>