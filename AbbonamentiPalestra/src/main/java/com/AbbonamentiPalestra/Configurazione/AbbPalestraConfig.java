package com.AbbonamentiPalestra.Configurazione;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.Scope;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.Abbonati;
import com.AbbonamentiPalestra.Class.Recensioni;

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
	
	@Bean("recensioni")
    @Scope("prototype")
    public Recensioni recensioni() {
        return new Recensioni();
    }
}
