<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { createParticipants } from '../api/participants'
// const props = defineProps([''])

const listCreated = ref(false)
const participantList = defineModel({ type: String })

async function createList() {
  const participantSet:Set<string> = new Set(participantList.value?.split('\n'))
  await createParticipants(participantSet)
  listCreated.value = true
}

</script>
<template>
  <main>
    <label for="p-list">Paste your participant list, one line per participant</label>
    <textarea v-model="participantList" id="p-list" name="" cols="30" rows="10" placeholder="participants..."></textarea>
    <button class="create-btn" @click="createList">Create</button>
    <p v-if="listCreated">
    Participant list created. You can go back to the <RouterLink to="/">home page</RouterLink>.
    </p>
  </main>
</template>

<style scoped>
  .create-btn {
    display: block;
  }
</style>
