<template>
  <VCalendar/>
  <DatePicker borderless expanded v-model="date" show-weeknumbers view="weekly"/>
</template>

<script>
import { VCalendar, DatePicker } from 'v-calendar';
import 'v-calendar/style.css';

export default {
  components: {
    VCalendar,
    DatePicker,
  },
  data() {
    return {
      date: new Date(),
    };
  },
}
</script>

