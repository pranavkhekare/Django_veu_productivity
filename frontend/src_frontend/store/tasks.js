export const state = () => ({
  list: [{ text: 'Text', done: false }]
})

export const mutations = {
  add (state, text) {
    state.list.push({
      text,
      done: false
    })
  },
  edit (state, payload) {
    const { index, text } = payload
    const updatetask = {
      ...state.list[index],
      text
    }
    state.list.splice(index, 1, updatetask)
  },
  remove (state, index) {
    state.list.splice(index, 1)
  },
  toggle (state, todo) {
    todo.done = !todo.done
  }
}
