<template>
  <v-card
    class="animated flipInX mx-auto"
    color="#26c6da"
    theme="dark"
    te
    v-if="show"
  >
    <v-card-text class="py-8" style="padding: 50px">
      <v-row align="center" hide-gutters no-gutters>
        <v-col class="text-h6" align="center"> Word: </v-col>
      </v-row>
      <v-row align="center" hide-gutters no-gutters>
        <v-col class="text-h1" align="center"> Key </v-col>
      </v-row>
      <v-row align="center" hide-gutters no-gutters>
        <v-col class="text-h1" align="center">
          <v-btn flat @click="show = !show"> Meaning </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
  <v-card
    class="animated flipInX mx-auto"
    color="#952175"
    theme="dark"
    max-width="800"
    v-if="!show"
  >

    <v-card-text class="py-8" style="padding: 50px">
      <v-row align="center" hide-gutters no-gutters>
        <v-col class="text-h3" align="center"> Key 
          <p class="text-h6" > [/kiː/]       <v-btn
        color="secondary"
        icon="mdi-play"
        size="x-small"
        @click.prevent="playSound('https://api.dictionaryapi.dev/media/pronunciations/en/key-uk.mp3')"
      ></v-btn></p>
          <p class="text-h6" > [/ki/]
                <v-btn
        color="secondary"
        icon="mdi-play"
        size="x-small"
        @click.prevent="playSound('https://api.dictionaryapi.dev/media/pronunciations/en/key-us.mp3')"
      ></v-btn>
          </p>
          </v-col>
      </v-row>
      <br>
      <v-row align="center" hide-gutters no-gutters>
        <v-col class="text-h6">
          <p class="text"><b>Definition:</b> (noun) An object designed to open and close a lock.</p> 
          <br>
        <p><b>Example:</b> "What are your key skills? What are your key skills? What are your key skills? What are your key skills?"</p>
        </v-col>
      </v-row>
      <br>
      <v-row align="center" hide-gutters no-gutters>
        <v-col>
          <p class="text-h6">Meanings</p>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-title>Key - noun</v-expansion-panel-title>
              <v-expansion-panel-text>
                <p>1. An object designed to fit between two other object…echanism and maintain their relative orientation.</p>
                <p>2. A crucial step or requirement.</p>
                <p>3. A guide explaining the symbols or terminology of a map or chart; a legend.</p>
                <p>4. A guide to the correct answers of a worksheet or test.</p>
                <p>5. One of several small, usually square buttons on a …eyboard, mostly corresponding to text characters.</p>
                <p>6.In musical instruments, one of the valve levers us…es, such as a lever opening a hole on a woodwind.</p>
                <p>A password restricting access to an IRC channel.</p>
                                <p>An object designed to fit between two other object…echanism and maintain their relative orientation.</p>
                <p>A crucial step or requirement.</p>
                <p>A guide explaining the symbols or terminology of a map or chart; a legend.</p>
                <p>A guide to the correct answers of a worksheet or test.</p>
                <p>One of several small, usually square buttons on a …eyboard, mostly corresponding to text characters.</p>
                <p>In musical instruments, one of the valve levers us…es, such as a lever opening a hole on a woodwind.</p>
                <p>A password restricting access to an IRC channel.</p>
                                <p>An object designed to fit between two other object…echanism and maintain their relative orientation.</p>
                <p>A crucial step or requirement.</p>
                <p>A guide explaining the symbols or terminology of a map or chart; a legend.</p>
                <p>A guide to the correct answers of a worksheet or test.</p>
                <p>One of several small, usually square buttons on a …eyboard, mostly corresponding to text characters.</p>
                <p>In musical instruments, one of the valve levers us…es, such as a lever opening a hole on a woodwind.</p>
                <p>A password restricting access to an IRC channel.</p>
                                <p>An object designed to fit between two other object…echanism and maintain their relative orientation.</p>
                <p>A crucial step or requirement.</p>
                <p>A guide explaining the symbols or terminology of a map or chart; a legend.</p>
                <p>A guide to the correct answers of a worksheet or test.</p>
                <p>One of several small, usually square buttons on a …eyboard, mostly corresponding to text characters.</p>
                <p>In musical instruments, one of the valve levers us…es, such as a lever opening a hole on a woodwind.</p>
                <p>A password restricting access to an IRC channel.</p>
                                <p>An object designed to fit between two other object…echanism and maintain their relative orientation.</p>
                <p>A crucial step or requirement.</p>
                <p>A guide explaining the symbols or terminology of a map or chart; a legend.</p>
                <p>A guide to the correct answers of a worksheet or test.</p>
                <p>One of several small, usually square buttons on a …eyboard, mostly corresponding to text characters.</p>
                <p>In musical instruments, one of the valve levers us…es, such as a lever opening a hole on a woodwind.</p>
                <p>A password restricting access to an IRC channel.</p>
              </v-expansion-panel-text>
            </v-expansion-panel>

            <v-expansion-panel>
              <v-expansion-panel-title>Key - verb</v-expansion-panel-title>
              <v-expansion-panel-text>
                Some content
              </v-expansion-panel-text>
            </v-expansion-panel>

            <v-expansion-panel>
              <v-expansion-panel-title>Key - adjective</v-expansion-panel-title>
              <v-expansion-panel-text>
                Some content
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>

    </v-card-text>

    <v-card-actions>
      <v-list-item class="w-100">
        <div class="d-flex justify-end">
          <v-icon class="mr-1" icon="mdi-thumb-up"></v-icon>
          <span class="subheading mr-2">256</span>
          <span class="mr-1">·</span>
          <v-icon class="mr-1" icon="mdi-thumb-down"></v-icon>
          <span class="subheading">45</span>
        </div>
      </v-list-item>
          <v-card-title>
      <v-btn flat @click="show = !show">OK</v-btn>
    </v-card-title>
    </v-card-actions>
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
  name: "FlashCard",
  methods: {
    playSound (sound) {
      if(sound) {
        var audio = new Audio(sound);
        audio.play();
      }
    }
  },
  data: () => ({
    drawer: false,
    group: null,
    show: true,
          open: ['Users'],
      admins: [
        ['Management', 'mdi-account-multiple-outline'],
        ['Settings', 'mdi-cog-outline'],
      ],
      cruds: [
        ['Create', 'mdi-plus-outline'],
        ['Read', 'mdi-file-outline'],
        ['Update', 'mdi-update'],
        ['Delete', 'mdi-delete'],
      ],
    items: [
      {
        title: "Foo",
        value: "foo",
      },
      {
        title: "Bar",
        value: "bar",
      },
      {
        title: "Fizz",
        value: "fizz",
      },
      {
        title: "Buzz",
        value: "buzz",
      },
    ],
  }),

  watch: {
    group() {
      this.drawer = false;
    },
  },
};
</script>
