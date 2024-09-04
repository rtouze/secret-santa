<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'
import { getParticipants, generateDraw as apiGenerateDraw, getDraws} from '../api/participants'

const participants = ref([])
const draws = ref([])

onBeforeMount(async () => { 
  console.log("before mount")
  const p = await getParticipants()
  console.debug("p",p)
  participants.value = p
  const d = await getDraws()
  draws.value = d
  console.debug("d",d)
})

async function generateDraw(event) {
  await apiGenerateDraw()
  draws.value = await getDraws()
}
</script>

<template>
  <main>
    <h2>Participant list</h2>
    <div v-if="participants.length">
      <div v-for="p in participants">
        {{p.name}}
      </div>
      <button @click="generateDraw">Generate draw</button>
    </div>
    <div v-else>No participant at the moment</div>
    <h2>Draw list</h2>
      <div v-for="d in draws">
        <div class="draw-date">Draw created at {{d.date}}</div>
        <ul>
          <li v-for="item in d.items"><strong>{{item.name}}</strong> offers to <strong>{{item.offers_to}}</strong></li>
        </ul>
      </div>
  </main>
</template>
