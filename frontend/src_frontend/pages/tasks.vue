<template>
  <v-container>
    <v-row>
      <v-col sm="6" offset-sm="3">
        <h1>Tasks</h1>
        <v-text-field
          v-model="new_task"
          label="Enter task (press enter)"
          @keypress.enter="add_task"
        />
        <v-list dense>
          <v-list-item-group color="primary">
            <v-list-item v-for="(todo, i) in list" :key="i">
              <template v-slot:default="{ active }">
                <v-list-item-action>
                  <v-checkbox
                    :input-value="active"
                  />
                </v-list-item-action>
                <v-list-item-content>
                  <span
                    v-if="editing_task.index === i"
                    class="d-flex justify-space-between align-center"
                  >
                    <v-text-field
                      v-model="editing_task.text"
                      @keypress.enter="save_edit"
                    />
                    <v-icon @click.stop="save_edit">
                      mdi-check
                    </v-icon>
                    <v-icon @click.stop="cancel_edit()">
                      mdi-cancel
                    </v-icon>
                  </span>
                  <span
                    v-else
                    class="d-flex justify-space-between align-center"
                  >
                    {{ todo.text }}
                    <span>
                      <v-icon @click.stop="edit_task(i)">
                        mdi-pencil
                      </v-icon>
                      <v-icon @click.stop="remove(i)">
                        mdi-delete-outline
                      </v-icon>
                    </span>
                  </span>
                </v-list-item-content>
              </template>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  data () {
    return {
      new_task: '',
      editing_task: {
        index: -1,
        text: ''
      }
    }
  },
  computed: {
    ...mapState('tasks', ['list'])
  },
  methods: {
    ...mapMutations('tasks', ['add', 'edit', 'remove', 'toggle']),
    add_task () {
      this.add(this.new_task)
      this.new_task = ''
    },
    edit_task (index) {
      this.editing_task.index = index
      this.editing_task.text = this.list[index].text
    },
    cancel_edit () {
      this.editing_task.index = -1
      this.editing_task.text = ''
    },
    save_edit () {
      this.edit(this.editing_task)
      this.cancel_edit()
    }
  }
}
</script>
