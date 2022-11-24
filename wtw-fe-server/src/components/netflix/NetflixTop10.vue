<template>
  <div id="netflixtop10">
    <h1>NETFLIX TOP 10</h1>
    <div v-if="netflixList.length != 0" class="horizontal_scroll">
      <b-row class="netflix-div">
        <movie-item class="child" v-for="(movieItem, index) in netflixList" :key="index" :movieItem="movieItem">
        </movie-item>
      </b-row>
    </div>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall.js'
import MovieItem from '@/components/MovieItem.vue'

export default {
  name: 'NetflixTop10',
  components: {
    MovieItem
  },
  data() {
    return {
      netflixList: [],
      isDown: false,
      startX: 0,
      scrollLeft: 0,
    }
  },
  methods: {
    getNetflixData() {
      const promiseRes = axiosCall('api/netflix/', 'get')
      promiseRes.then((data) => this.netflixList = data)
    },
    // scrollmousedown(event){
    //   console.log('scrollmousedown')
    //   const slider = document.querySelector('.netflix-div')
    //   this.isDown = true;
    //   // slider.classList.add('active');
    //   this.startX = event.pageX - slider.offsetLeft;
    //   this.scrollLeft = slider.scrollLeft;
    //   console.log(slider)
    //   console.log(event.target)
    // },

    // scrollmouseleave(){
    //   console.log('scrollmouseleave')
    //   // const slider = document.querySelector('.netflix-div')
    //   this.isDown = false;
    //   // slider.classList.remove('active');
    // },

    // scrollmouseup(){  
    //   console.log('scrollmouseup')
    //   // const slider = document.querySelector('.netflix-div')
    //   this.isDown = false;
    //   // slider.classList.remove('active');
    // },

    // scrollmousemove(event){
    //   console.log('scrollmousemove')
    //   const slider = document.querySelector('.netflix-div')
    //   if (!this.isDown) return;
    //   event.preventDefault()
    //   const x = event.pageX - slider.offsetLeft
    //   const walk = x - this.startX;
    //   console.log(walk)
    //   slider.style.transform += `translateX(${walk}px)`;
    // },
    // getTranslateX() {
    //   const slider = document.querySelector('.netflix-div')
    //   return parseInt(getComputedStyle(slider).transform.split(/[^\-0-9]+/g)[5]);
    //   },
    // getClientX(e) {
    //   const isTouches = e.touches ? true : false;
    //   return isTouches ? e.touches[0].clientX : e.clientX;
    // },
    //    onScrollEnd(e) {
    //      endX = getClientX(e);
    //      listX = getTranslateX();
    //      if (listX > 0) {
    //        setTranslateX(0);
    //        list.style.transition = `all 0.3s ease`;
    //        listX = 0;
    //      } else if (listX < listClientWidth - listScrollWidth) {
    //        setTranslateX(listClientWidth - listScrollWidth);
    //        list.style.transition = `all 0.3s ease`;
    //        listX = listClientWidth - listScrollWidth;
    //      }
    //
    //      window.removeEventListener('mousedown', onScrollStart);
    //      window.removeEventListener('touchstart', onScrollStart);
    //      window.removeEventListener('mousemove', onScrollMove);
    //      window.removeEventListener('touchmove', onScrollMove);
    //      window.removeEventListener('mouseup', onScrollEnd);
    //      window.removeEventListener('touchend', onScrollEnd);
    //      window.removeEventListener('click', onClick);
    //
    //      setTimeout(() => {
    //        bindEvents();
    //        list.style.transition = '';
    //      }, 300);
    //    }

  },
  created() {
    this.getNetflixData()
  }
}
</script>

<style>
#netflixtop10 {
  color: white !important;
  margin: 20px;
}
</style>