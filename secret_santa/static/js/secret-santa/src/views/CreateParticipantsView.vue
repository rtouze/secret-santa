<script setup lang="ts">
import { ref } from 'vue'
import { createParticipants } from '../api/participants'
// const props = defineProps([''])

const participantList = defineModel()
let pSet = ref([])

async function createList(event) {
  console.log('createList clicked')
  console.log(participantList)
  const participantSet = new Set(participantList.value.split('\n'))
  console.log(participantSet)
  pSet.value = Array.from(participantSet.values())
  createParticipants(participantSet)
}

</script>
<template>
  <main>
    <label for="p-list">Paste your participant list, one line per participant</label>
    <textarea v-model="participantList" id="p-list" name="" cols="30" rows="10" placeholder="participants..."></textarea>
    <pre>
    content
    {{pSet}}
    </pre>
    <button @click="createList">Create</button>
  </main>
</template>
