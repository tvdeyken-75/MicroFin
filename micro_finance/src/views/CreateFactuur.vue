<script>
import axios from 'axios';

export default {
  data() {
    return {
      factuur: {
        factuurNummer: '',
        regels: []
      }
    };
  },
  methods: {
    voegRegelToe() {
      this.factuur.regels.push({
        omschrijving: '',
        bedrag: 0
      });
    },
    verwijderRegel(index) {
      this.factuur.regels.splice(index, 1);
    },
    async submitFactuur() {
      try {
        // Hier post je de hoofdfactuur
        const response = await axios.post('http://localhost:9000/api/facturen', this.factuur);
        const factuurId = response.data.id;

        // Post elke factuurregel naar de API
        for (let regel of this.factuur.regels) {
          await axios.post(`http://localhost:9000/api/factuurregels/${factuurId}`, regel);
        }

        alert('Factuur en regels succesvol aangemaakt!');
      } catch (error) {
        console.error('Fout tijdens het aanmaken van factuur en regels:', error);
        alert('Er is een fout opgetreden.');
      }
    }
  }
};
</script>
