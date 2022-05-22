<template>
  <v-card>
    <v-layout>
      
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/men/1.jpg"
            title="First Last"
            subtitle="email@gmailcom"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-folder" title="My Files" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-account-multiple" title="Shared with me" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Starred" value="starred"></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar
        color="white" 
      >
        <v-app-bar-title>Learning Job Interview terms App</v-app-bar-title>

        <template v-slot:append>
          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
      </v-app-bar>

      <v-main><v-container><FlashCard /></v-container></v-main>
    </v-layout>
  </v-card>
</template>

<script>
import FlashCard from './components/FlashCard.vue'

export default {
  name: 'App',

  components: {
    FlashCard,
  },

  data: () => ({
    //
  }),
}
</script>
