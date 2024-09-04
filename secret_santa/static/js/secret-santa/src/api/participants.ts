const BASE_API_URL = 'http://127.0.0.1:8000'

export async function createParticipants(pSet:Set<string>) {
  const plist = Array.from(pSet.values())
  try {
  const resp = await fetch(BASE_API_URL + "/api/v1/participants", {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify({'plist':plist}),
  })
  }
  catch (e) {
    console.error(e)
  }
}

export async function getParticipants() {
  try {
    const resp = await fetch(BASE_API_URL + "/api/v1/participants", {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    })
    const data = await resp.json()
    console.log("participant data", data)
    return data.data

  }
  catch (e) {
    console.error(e)
  }
}

export async function generateDraw() {
  const resp = await fetch(BASE_API_URL + "/api/v1/draw", { method: 'POST', headers: {'Content-type': 'application/json'}})
}

export async function getDraws() {
  const resp = await fetch(BASE_API_URL + "/api/v1/draw", { method: 'GET', headers: {'Accept': 'application/json'}})
  const data = await resp.json()
  return data.data
}
