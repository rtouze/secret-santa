<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <h1>Secret Santa</h1>
    <ul>
      <li>
        <RouterLink to="/">Home</RouterLink>
      </li>
      <li>
        <RouterLink to="/create-participant-list">Create a participant list</RouterLink>
      </li>
    </ul>
  </header>
  <RouterView />
</template>

<style scoped></style>
