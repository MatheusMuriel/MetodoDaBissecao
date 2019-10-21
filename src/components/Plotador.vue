<template>
  <div id="plotador">
      <div id="myFunction"></div>
  </div>
</template>

<script>
export default {
  name: 'plotador',
  props: {
    title: String,
    gn: String,
    hn: String,
    grid: Boolean
  },
  created () {
    return this.plot()
  },
  methods: {
    plot () {
      this.$loadScript('https://unpkg.com/d3@3/d3.min.js')
        .then(() => {
          this.$loadScript('https://unpkg.com/function-plot@1/dist/function-plot.js')
            .then(() => {
              var parameters = {
                target: '#myFunction',
                title: this.$props.title,
                data: [{fn: this.$props.gn}, {fn: this.$props.hn}],
                grid: this.$props.grid
              }
              // eslint-disable-next-line
              functionPlot(parameters)
            })
            .catch((e) => {
              console.log(e)
              console.log("Falha no 'function-plot.js'")
            })
        })
        .catch((e) => {
          console.log(e)
          console.log("Falha no 'd3.min.js'")
        })
    }
  }
}
</script>
