<template>
<div class="tasks">
  <div>{{ answer }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TasksView",
  data() {
    return {
      answer: {},
    };
  },
  methods: {
    async getAnswer() {
      const { data } = await axios.get("http://127.0.0.1:8000/api/todoTask");
      this.answer = data;
    },
  },
  beforeMount() {
    this.getAnswer();
  },
};
</script>