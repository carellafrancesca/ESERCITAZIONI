package com.AbbonamentiPalestra.Configurazione;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.Scope;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.Abbonati;
import com.AbbonamentiPalestra.Class.UtenteAccesso;

@Configuration
@PropertySource("classpath:application.properties")
public class AbbPalestraConfig {

	@Bean("abbonati")
    @Scope("prototype")
    public Abbonati abbonati() {
        return new Abbonati();
    }
	
	@Bean("abbonamenti")
    @Scope("prototype")
    public Abbonamenti abbonamenti() {
        return new Abbonamenti();
    }
	
	@Bean("utenteAccesso")
    @Scope("prototype")
    public UtenteAccesso utente() {
        return new UtenteAccesso();
    }
	
}
