<script setup lang="ts">
import {ref} from 'vue'
import { updateParticipantBlacklist } from '../api/participants'

const props = defineProps(['participant'])
const blackList = ref(props.participant.blacklist.join('\n'))
const isInEditionMode = ref(false)

function toggleEdit() {
  isInEditionMode.value = !isInEditionMode.value
}

async function updateBlacklist() {
  props.participant.name
  const blacklistAsArray = blackList.value?.split('\n')
  const newBlacklist = await updateParticipantBlacklist(props.participant.name, blacklistAsArray)
  blackList.value = newBlacklist.join('\n')
  toggleEdit()
}

</script>
<template>
  <div class="participant">
    <div>
      <strong>{{props.participant.name}}</strong>
      <button class="edit-button" @click="toggleEdit">
        <span v-if=isInEditionMode>Cancel</span>
        <span v-else>Edit blacklist</span>
      </button>
    </div>
    <div v-if="isInEditionMode">
      <div>Edit participant blacklist</div>
      <textarea placeholder="paste participant's blacklist" v-model="blackList" cols="30" rows="10"></textarea>
      <button class="update-blacklist-button" @click="updateBlacklist">Update blacklist</button>
    </div>
    <div v-else>
      <span class="read-blacklist" v-if="blackList">
      Blacklist : {{ blackList.replaceAll('\n', ', ') }}
      </span>
      <span class="read-blacklist" v-else>No blacklisted participant</span>
    </div>
  </div>
</template>
<style scoped>
.participant {
  margin-bottom: 1rem;
}

.edit-button {
  margin-left: 2rem;
}

.read-blacklist {
  font-style: italic;
  color: gray;
}

.update-blacklist-button {
  display: block;
}
</style>
