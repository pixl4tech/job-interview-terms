<template>
  <v-card>
    <v-layout>
      <!-- <v-system-bar color="deep-purple darken-3"></v-system-bar> -->

      <v-app-bar
        color="primary"
        prominent
      >
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>My files</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn variant="text" icon="mdi-magnify"></v-btn>

        <v-btn variant="text" icon="mdi-filter"></v-btn>

        <v-btn variant="text" icon="mdi-dots-vertical"></v-btn>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        bottom
        temporary
      >
        <v-list
          :items="items"
        ></v-list>
      </v-navigation-drawer>

      <v-main>
        <v-card-text>
          The navigation drawer will appear from the bottom on smaller size screens.
        </v-card-text>
        <v-card
          class="animated flipInX mx-auto"
          color="#26c6da"
          theme="dark"
          max-width="400"
          v-if="show"
        >
          <v-card-title>
            <v-icon
              size="large"
              left
              icon="mdi-twitter"
            ></v-icon>
            <span class="text-h6 font-weight-light">Twitter</span>
          </v-card-title>

          <v-card-text class="text-h5">
            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
          </v-card-text>

          <v-card-actions>
            <v-list-item class="w-100">
              <v-list-item-avatar left>
                <v-avatar
                  @click="show=!show"
                  color="grey-darken-3"
                  image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-avatar>
              </v-list-item-avatar>

              <v-list-item-header>
                <v-list-item-title>Evan You</v-list-item-title>
              </v-list-item-header>

              <div class="d-flex justify-end">
                <v-icon class="mr-1" icon="mdi-heart"></v-icon>
                <span class="subheading mr-2">256</span>
                <span class="mr-1">·</span>
                <v-icon class="mr-1" icon="mdi-share-variant"></v-icon>
                <span class="subheading">45</span>
              </div>
            </v-list-item>
          </v-card-actions>
        </v-card>
        <v-card
          class="animated flipInX mx-auto"
          color="#952175"
          theme="dark"
          max-width="800"
          v-if="!show"
        >
          <v-card-title>
            <v-icon
              size="large"
              left
              icon="mdi-twitter"
            ></v-icon>
            <span class="text-h6 font-weight-light">Twitter</span>
          </v-card-title>

          <v-card-text class="text-h5">
            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                  "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                  "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
          
          </v-card-text>

          <v-card-actions>
            <v-list-item class="w-100">
              <v-list-item-avatar left>
                <v-avatar
                  @click="show=!show"
                  color="grey-darken-3"
                  image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-avatar>
              </v-list-item-avatar>

              <v-list-item-header>
                <v-list-item-title>Evan You</v-list-item-title>
              </v-list-item-header>

              <div class="d-flex justify-end">
                <v-icon class="mr-1" icon="mdi-heart"></v-icon>
                <span class="subheading mr-2">256</span>
                <span class="mr-1">·</span>
                <v-icon class="mr-1" icon="mdi-share-variant"></v-icon>
                <span class="subheading">45</span>
              </div>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-main>
    </v-layout>
  </v-card>
</template>





<style>

.animated {
    animation-duration: 1s;
    animation-fill-mode: both;
}
@keyframes flipInX {
    from {
        transform: perspective(400px) rotate3d(1, 0, 0, 180deg);
        animation-timing-function: ease-in;
        opacity: 0;
    }
    40% {
        transform: perspective(400px) rotate3d(1, 0, 0, -20deg);
        animation-timing-function: ease-in;
    }
    60% {
        transform: perspective(400px) rotate3d(1, 0, 0, 10deg);
        opacity: 1;
    }
    80% {
        transform: perspective(400px) rotate3d(1, 0, 0, -5deg);
    }
    to {
        transform: perspective(400px);
    }
}
.flipInX {
    backface-visibility: visible !important;
    animation-name: flipInX;
}

</style>


<script>
  export default {
    name: 'HelloWorld',
    data: () => ({
      drawer: false,
      group: null,
      show: true,
      items: [
        {
          title: 'Foo',
          value: 'foo',
        },
        {
          title: 'Bar',
          value: 'bar',
        },
        {
          title: 'Fizz',
          value: 'fizz',
        },
        {
          title: 'Buzz',
          value: 'buzz',
        },
      ],
    }),

    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>
