<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <h1>Secret santa</h1>
    <RouterLink to="/create-participant-list">Create a participant list</RouterLink>
  </header>
  <RouterView />
</template>

<style scoped></style>
